---
name: sg-mala-optimiser-engine
description: Optimize Singapore Mala Xiang Guo and Malatang bowls under a fixed budget (e.g. $30 SGD) to either minimize restaurant profit margins (maximize wholesale/retail COGS recovery across NTUC FairPrice, Sheng Siong, RedMart, Shopee, Lazada, Pasir Panjang Wholesale, Victoria Wholesale, Song Fish, and Fassler Gourmet) or maximize clinical nutritional health using HPB SGFoodID Recipe Analyser, SGFoodID Food Search, and Data.gov.sg Healthier Ingredient Development Scheme (HIDS d_cd7fbc766695f997396b96bf93820382). Also performs Continuous-Time Actuarial valuation of stored-value F&B memberships ($55 for $60 credit) and HPB Health Policy subsidy design.
---
# sg-mala-optimiser-engine

Quantitative dual-objective optimization, food-physics arbitrage, actuarial stored-value membership valuation, and public health policy engine for Singapore Mala Xiang Guo and Malatang restaurants in Antigravity IDE (Gemini 3.8 Flash).

## When to Use

- User wants to optimize a Mala Xiang Guo or Malatang order within a fixed budget (such as S$30.00) for maximum bang-for-bucks or minimum restaurant profit margin.
- User wants to compare ingredient baseline costs across NTUC FairPrice, Sheng Siong, RedMart/Lazada, Shopee Supermarket, Pasir Panjang Wholesale Centre (PPWC), Victoria Wholesale Centre (VWC), Song Fish, and Fassler Gourmet against restaurant pricing architectures (Unified Weight per 100g, Tiered Weight per 100g, or Fixed Per-Portion hawker stalls).
- User wants to evaluate pre-weighing water soakage physics, ice-glaze weight traps, post-weighing oil absorption, or unlimited free-flow bar economics (steamed rice, soup refills, spiced peanuts, prawn crackers, sour plum drinks, ice jelly, and soft-serve ice cream).
- User wants to evaluate whether a prepaid restaurant membership (such as S$60 credit for S$55 upfront cash) is a winning or losing deal given Singapore ACRA/SingStat F&B closure hazard rates, restaurant COGS liabilities, breakage, residual balance trapping, and forgone credit card rewards.
- User wants to optimize a Mala bowl for health and longevity using the HPB SGFoodID Recipe Analyser (`https://pphtpc.hpb.gov.sg/web/sgfoodid/tools/recipe-analyser`), SGFoodID Food Search (`https://pphtpc.hpb.gov.sg/web/sgfoodid/tools/food-search`), and Data.gov.sg HIDS Partner List ([`d_cd7fbc766695f997396b96bf93820382`](https://data.gov.sg/datasets/d_cd7fbc766695f997396b96bf93820382/view)), or design HPB health policy subsidies across dry and soup Mala variations.

## Core Mathematical & Graph Engineering Architecture

1. **Pre-Weighing Hydration & Scale Arbitrage Physics**

   - At weight-based chains (such as Yang Guo Fu, Zhang Liang, Gong Yuan, and A Hot Hideout charging S$2.68 to S$3.25 per 100g), ingredients are weighed raw before cooking.
   - Pre-soaked items absorb water by factor $\gamma_{\text{wet}} \ge 1.0$, reducing the restaurant's effective wet-weighed wholesale cost to:
     $$\text{COGS}_{\text{wet}, i} = \frac{\text{COGS}_{\text{dry}, i}}{\gamma_{\text{wet}, i}}$$
   - Conversely, picking dry ring rolls (*ling ling juan*), dry fried *tau kee*, *tau pok*, and dry instant noodles ($\gamma_{\text{wet}} = 1.0$) shifts expansion to the post-weighing cooking phase.

2. **Dual-Objective $30 Budget Knapsack & Cellular Sheaf Hypergraph**

   - **Objective A (Margin Crusher / Bang-for-Bucks)**:
     $$\max_{w_i} \sum_{i=1}^{96} w_i \cdot \frac{\text{COGS}_{\text{wet}, i}}{P_i(m)} + V_{\text{free-flow}} \quad \text{s.t.} \quad \sum_{i=1}^{96} w_i P_i(m) + P_{\text{base}} \le 30.00$$
   - **Objective B (HPB SGFoodID & HIDS Clinical Health Optimiser)**:
     $$\max_{w_i} \sum_{i=1}^{96} w_i \left(1.8 \text{Prot}_i + 3.2 \text{Fib}_i - 1.5 \text{SatFat}_i - \frac{\text{Sod}_i}{250} - 2.5 \alpha_{\text{oil}, i}\right)$$
     subject to HPB Healthier Dining Programme (HDP) and My Healthy Plate constraints ($\le 500\text{--}700\text{ kcal/pax}$, $\ge 35\text{g protein/pax}$, $\ge 7\text{g fiber/pax}$, $\le 1,000\text{mg sodium/pax}$).

3. **Continuous-Time Actuarial Membership Valuation ($55 for $60)**

   - Models Singapore F&B insolvency as an inhomogeneous Poisson hazard process $\lambda(t)$ calibrated to ACRA/SingStat disclosures (2,916 F&B closures in Jan-Oct 2026; 63% closing within 5 years; 82% of closing young outlets never recording a taxable profit):
     $$\text{EV}_{\text{net}} = (C - M_0) - (M_0 - S_1)\left(1 - e^{-\lambda T}\right) - b \cdot C - \pi_{\text{menu}} C T - r_{\text{card}} C - r_{f} (M_0 - S_1) T$$

## Step-by-Step Workflow

1. **Query Singapore Supermarket/Wholesale Baselines & HIDS Partners**

   - Run `fetch_sg_supermarket_wholesale_prices` from `scripts/sg_mala_quant_mcp.py` to load the 96-item catalog with verified NTUC FairPrice, Sheng Siong, RedMart, Shopee, PPWC, VWC, Song Fish, and Fassler Gourmet baseline prices.
   - Run `query_datagov_hids_partners` to query Data.gov.sg resource [`d_cd7fbc766695f997396b96bf93820382`](https://data.gov.sg/datasets/d_cd7fbc766695f997396b96bf93820382/view) for HIDS-accredited healthier oils, wholegrain rice/noodles, and lower-sodium sauces/K-Salt.

2. **Solve the $30 Knapsack & Verify via SGFoodID Recipe Analyser**

   - Call `solve_mala_knapsack_30sgd` with `pricing_model` (`unified`, `tiered`, or `portion`) and `objective` (`minimise_restaurant_margin`, `maximise_health`, or `pareto_joint`).
   - Pass the resulting ingredient basket and chosen base (`B01` to `B14`) into `query_hpb_sgfoodid_recipe_analyser` and `scripts/mala_sheaf_hypergraph.py` to compute whole-pot and per-diner calories, protein, fiber, saturated fat, sodium, and Cellular Sheaf Laplacian consistency energy.

3. **Run Actuarial Membership & Health Policy Simulations**

   - Call `evaluate_mala_membership_actuarial` to compute the restaurant's true marginal COGS liability ($15.00-$21.00 on $60 credit), break-even visits (1.83 visits for principal recovery; 2-3 visits for full depletion), and net risk-adjusted EV across dining frequencies.

## Gotchas

- Never recommend pre-soaked starches (sweet potato noodles, *tang hoon*), pre-soaked dried fungi (wood ear, snow fungus, bamboo pith), or dense tubers (potato, white radish, lotus root) at unified-weight stalls when optimizing for financial value; route those items exclusively to fixed per-portion hawker stalls (such as Ri Ri Hong or Labula).
- Always distinguish between full-pot Malatang broth sodium (2,650-3,200mg) and actual ingested sodium when leaving 60%-70% of the soup base unconsumed.
