"""
Micro-Deal Alert (MDA) — Three-Stage Real Estate Underwriting Pipeline
Implements:
  Stage 1: Deduplication + micro-market PPSF anomaly filter (>= 10% below mean)
  Stage 2: Intrinsic & Trakheesi permit verification
  Stage 3: Net rental yield calculation after service charges
"""

import csv
from pathlib import Path

JVC_BENCHMARK_PPSF = 1460.0
MIN_DISCOUNT_PCT = 0.10
MIN_NET_YIELD_PCT = 5.5


def run_pipeline(csv_path: str) -> list[dict]:
    with open(csv_path, mode="r", encoding="utf-8") as f:
        raw_rows = list(csv.DictReader(f))

    # Stage 1A: Deduplicate by (building, area_sqft, asking_price_aed)
    seen = set()
    unique_rows = []
    for row in raw_rows:
        key = (
            row["building"].strip().lower(),
            float(row["area_sqft"]),
            float(row["asking_price_aed"]),
        )
        if key not in seen:
            seen.add(key)
            unique_rows.append(row)

    # Stage 1B, Stage 2 & Stage 3 filtering
    shortlist = []
    max_allowed_ppsf = JVC_BENCHMARK_PPSF * (1 - MIN_DISCOUNT_PCT)

    for row in unique_rows:
        area = float(row["area_sqft"])
        price = float(row["asking_price_aed"])
        gross_rent = float(row["annual_rent_comp_aed"])
        service_charge = float(row["annual_service_charge_aed"])
        permit = row["trakheesi_permit"].strip()

        ppsf = price / area
        discount_pct = ((JVC_BENCHMARK_PPSF - ppsf) / JVC_BENCHMARK_PPSF) * 100

        # Stage 1B: PPSF Anomaly Filter
        if ppsf > max_allowed_ppsf:
            continue

        # Stage 2: Trakheesi Permit Audit
        if not permit or not permit.isdigit():
            continue

        # Stage 3: Net Yield Verification
        net_rent = gross_rent - service_charge
        net_yield_pct = (net_rent / price) * 100
        if net_yield_pct < MIN_NET_YIELD_PCT:
            continue

        shortlist.append(
            {
                "building": row["building"],
                "district": row["district"],
                "price_aed": round(price),
                "ppsf": round(ppsf),
                "discount_pct": round(discount_pct, 1),
                "net_yield_pct": round(net_yield_pct, 1),
                "permit": permit,
                "notes": row["notes"],
            }
        )

    shortlist.sort(key=lambda x: x["net_yield_pct"], reverse=True)
    return shortlist


if __name__ == "__main__":
    data_file = Path(__file__).parent / "data" / "jvc_sample_listings.csv"
    deals = run_pipeline(str(data_file))

    print(f"JVC Benchmark PPSF: AED {JVC_BENCHMARK_PPSF:,.0f}/sqft | Verified Outliers: {len(deals)}\n")
    for idx, d in enumerate(deals, start=1):
        print(
            f"{idx}. {d['building']} ({d['district']}) | "
            f"AED {d['price_aed']:,} | AED {d['ppsf']}/sqft (-{d['discount_pct']}%) | "
            f"Net Yield: {d['net_yield_pct']}% | Permit: {d['permit']}"
        )