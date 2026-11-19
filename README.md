\# Micro-Deal Alert (MDA)

\*\*Productized Weekly Real Estate Outlier Intelligence for Brokers\*\*  

\*A product by \*\*REALEST — Capital \& Investments\*\*\*



Micro-Deal Alert (MDA) is a weekly intelligence subscription for real estate brokers. Each week, it delivers \*\*3–5 verified outlier listings\*\*—each backed by empirical price-per-square-foot deltas, verified Trakheesi permits, net yield math, a broker script, and a closing argument.



The core product is verified data and outlier identification; the broker talking points are complementary. A broker pays to be the best-informed person in the room, and the script simply helps them articulate the math.



> \*\*Sample Weekly Deliverable:\*\* \[View JVC Market Intelligence Sample Report (`samples/jvc\_micro\_deal\_alert\_sample.pdf`)](samples/jvc\_micro\_deal\_alert\_sample.pdf)



\---



\## How It's Built: Three-Stage Underwriting Stack



Only listings that survive all three filters ship—which is why the deliverable contains \*\*3–5 deals per week instead of 50\*\*:



1\. \*\*Stage 1 — Portal Scrub \& Deduplication:\*\*

&#x20;  \* Pulls raw listings from portals (PropertyFinder, 99acres, Magicbricks) and scrubs duplicate/ghost ads before ranking.

&#x20;  \* Compares each unique listing's price/sqft against the micro-market mean and filters for material price anomalies (e.g., for JVC, at least \*\*10% below AED 1,460/sqft\*\*).

2\. \*\*Stage 2 — Intrinsic Audit:\*\*

&#x20;  \* Separates genuine mispricing from value traps by verifying Trakheesi permit numbers, developer track records (e.g., Ellington, Binghatti, Damac), unit specifics (floor, view, handover status), and seller-motivation signals (`Motivated Seller`, `Urgent`, `OP` / Original Price).

&#x20;  \* A cheap listing with a handover delay, bad floor, or unverified permit is discarded as a warning rather than an outlier.

3\. \*\*Stage 3 — Net Yield Verification:\*\*

&#x20;  \* Computes true net yield using actual building-level rent comps:

&#x20;    $$\\text{Net Yield} = \\frac{\\text{Gross Annual Rent} - \\text{Annual Service Charges}}{\\text{Asking Price}}$$

&#x20;  \* A price discount only ships if net rental yield supports the entry valuation.



\---



\## Weekly Deliverable Structure



Each weekly dispatch features \*\*3–5 curated listings\*\* alongside market-noise telemetry and deal-specific leverage:

\* \*\*Data Block:\*\* Asking price, PPSF vs. district mean (`%` equity gap), verified net yield, and Trakheesi permit number.

\* \*\*Operational Leverage:\*\* Quantifies portal noise scrubbed (e.g., eliminating 32% duplicate/ghost listings across 167 raw JVC entries) so brokers only call real sellers with verified titles.

\* \*\*Marketing \& Closing Leverage:\*\* Concise, data-backed talking points tailored to buyer profiles (immediate equity gap, low-ticket entry near high-footfall retail, or motivated OP liquidity exits) to neutralize buyer's remorse objections upfront.



\---



\## Live Run Lessons (JVC Benchmark)



Running Stages 1 and 3 on a live JVC portal dataset surfaced two critical engineering requirements for automated v2 pipelines:



1\. \*\*Deduplicate Before Ranking:\*\* 51 rows cleared the 10% below-mean filter, but collapsed into just \*\*6 unique listings\*\* once repeat scraper entries were removed. Without strict deduplication, any "Top 3" list is invalid.

2\. \*\*Building-Specific Rent Comps:\*\* Applying a flat AED 90/sqft rent assumption reduces net yield to $\\frac{75}{\\text{PPSF}}$, turning yield ranking into a duplicate of price ranking. Stage 3 only adds independent signal when fed building-level rental comps.



\*\*Six Unique JVC Candidates Identified:\*\*

\* \*\*Fortunato:\*\* AED 969/sqft | 7.7% net yield

\* \*\*Aria:\*\* AED 1,029/sqft | 7.3% net yield

\* \*\*Ghalia Tower (District 18):\*\* AED 1,081/sqft (26% below mean) | 6.9% net yield | Trakheesi `7117805799`

\* \*\*Q Gardens Lofts (District 13):\*\* AED 1,174/sqft (20% below mean) | 6.4% net yield | Trakheesi `71426359489`

\* \*\*Plaza Residences:\*\* AED 1,221/sqft | 6.1% net yield

\* \*\*RA1N Residence (District 12):\*\* AED 1,241/sqft (15% below mean) | 6.0% net yield | Trakheesi `71500643100` (\*Motivated Seller / OP\*)



\---



\## Pricing Strategy (Dubai Market)



| Tier | Price | Positioning |

| :--- | :--- | :--- |

| \*\*Weekly\*\* | AED 250 (\~₹6,000) | Intro / trial tier (significantly underpriced for Dubai) |

| \*\*Monthly\*\* | AED 1,000 (\~₹24,500) | Early-adopter rate (significantly underpriced) |

| \*\*Target Monthly\*\* | \*\*AED 2,000 – 3,500 / month\*\* | Standard B2B subscription once case studies are established |



At \*\*AED 2,500/month\*\*, 10 subscribers generate \*\*AED 25,000/month (\~₹6,00,000)\*\* against \~₹1,700/month in AI tooling costs plus analyst time.



\---



\## Repository Structure



```text

micro-deal-alert/

├── samples/

│   └── jvc\_micro\_deal\_alert\_sample.pdf   # 4-page sample JVC broker intelligence report

└── README.md                             # Underwriting stack, JVC audit findings \& pricing model

