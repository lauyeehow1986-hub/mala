# Singapore Mala Xiang Guo & Malatang Multi-Objective Quant Optimiser, Cellular Sheaf Hypergraph, Actuarial Membership Engine & HPB Health Policy Simulator

Quantitative dual-objective optimization, food-physics arbitrage, actuarial stored-value membership valuation, and public health policy simulation engine for Singapore Mala Xiang Guo and Malatang restaurants in **Antigravity IDE (Gemini 3.8 Flash)**.

---

## 1. Architecture Overview

This repository provides an integrated operations research and health policy platform:
- **`mcp_servers/sg_mala_quant_mcp.py`**: A model context protocol server exposing 5 tools for knapsack optimization, actuarial credit valuation, supermarket/wholesale cost baseline lookups, and HPB SGFoodID recipe simulation.
- **`graph_engineering/mala_sheaf_hypergraph.py`**: A Heterogeneous Cellular Sheaf Hypergraph $G = (V, E, \mathcal{F})$ enforcing hydration restrictions ($\gamma_{\text{wet}}$), lipid-sodium restrictions ($\alpha_{\text{oil}}$), and computing Sheaf Laplacian Cohomology Energy $\mathcal{E}(x) = \| L_{\mathcal{F}} x \|_2^2$.
- **`data/`**: Exhaustive 96-item Singapore Mala catalog benchmarked against NTUC FairPrice, Sheng Siong, RedMart/Lazada, Shopee Supermarket, Pasir Panjang Wholesale Centre (PPWC), Victoria Wholesale Centre (VWC), Song Fish Dealer, and Fassler Gourmet; 14 Broth & Sauce Bases (`B01` to `B14`); and HPB HIDS Partner List (`d_cd7fbc766695f997396b96bf93820382`).
- **`hooks/` & `.agents/hooks.json`**: Pre-tool guards enforcing the fixed $\$30.00$ SGD budget cap and post-tool audits verifying clickable Singapore supermarket deep links and Sheaf Cohomology.
- **`skills/sg-mala-optimiser-engine/`**: Antigravity IDE custom skill for automated quant optimization and policy simulations.

---

## 2. Core Capabilities & MCP Tools

1. **`fetch_sg_supermarket_wholesale_prices`**:
   - Queries baseline costs across 96 items spanning 10 categories (Leafy Veg, Root/Stem/Cruciferous, Fungi, Soy, Noodles/Starches, Surimi/Balls, Meat Cuts, Offal/Tripe, Seafood, Specialty Delicacies).
2. **`solve_mala_knapsack_30sgd`**:
   - Continuous/discrete bounded knapsack solver across Unified Weight ($\$2.98/100\text{g}$), Tiered Weight ($\$1.50\text{--}\$3.50/100\text{g}$), and Fixed Per-Portion hawker stall pricing models.
   - Objectives: `minimise_restaurant_margin`, `maximise_health`, and `pareto_joint`.
3. **`query_hpb_sgfoodid_recipe_analyser`**:
   - Simulates the HPB Singapore Food Insights Database (SG FoodID) [Recipe Analyser](https://pphtpc.hpb.gov.sg/web/sgfoodid/tools/recipe-analyser) and [Food Search](https://pphtpc.hpb.gov.sg/web/sgfoodid/tools/food-search).
   - Computes calories, protein, saturated fat, and sodium per diner against Healthier Dining Programme (HDP) thresholds ($\le 500\text{--}700\text{ kcal}$, $\le 1,000\text{mg sodium}$).
4. **`query_datagov_hids_partners`**:
   - Interfaces with the Data.gov.sg CKAN datastore ([`d_cd7fbc766695f997396b96bf93820382`](https://data.gov.sg/datasets/d_cd7fbc766695f997396b96bf93820382/view)) for HPB Healthier Ingredient Development Scheme (HIDS) suppliers of healthier oils ($\le 35\%$ sat fat), wholegrains, and potassium-enriched K-Salt.
5. **`evaluate_mala_membership_actuarial`**:
   - Evaluates stored-value top-up packages (e.g. $\$60$ credit for $\$55$ upfront cash) under inhomogeneous Poisson F&B closure hazard rates ($\lambda_{\text{base}} = 14\%$, $\lambda_{\text{young}} = 22\%$, $\lambda_{\text{distress}} = 45\%$) calibrated to ACRA/SingStat disclosures.

---

## 3. Directory Layout

```
mala/
├── .agents/
│   └── hooks.json                                                # Antigravity IDE PreToolUse & PostToolUse hooks
├── data/
│   ├── hpb_hids_partners_d_cd7fbc766695f997396b96bf93820382.csv # HPB HIDS Partner List
│   ├── mala_14_bases_nutrition.csv                              # 14 Broth & Sauce Bases nutrition & oil profiles
│   └── sg_mala_96_ingredients_catalog.csv                       # 96 ingredients with wholesale/retail baselines & soak ratios
├── graph_engineering/
│   └── mala_sheaf_hypergraph.py                                 # Cellular Sheaf Hypergraph Laplacian engine
├── hooks/
│   ├── post_solve_sheaf_audit.py                                # PostToolUse Sheaf Cohomology & URL grounding audit
│   └── pre_tool_mala_guard.py                                   # PreToolUse $30 budget cap & water trap guard
├── mcp_servers/
│   └── sg_mala_quant_mcp.py                                     # FastMCP / MCPServer 2.x implementation
├── reports/
│   ├── mediterranean_hpb_optimal_bowl_analysis.md               # Mediterranean Diet × HPB clinical & flavor simulation report
│   ├── multi_quantum_bang_for_bucks_report.md                   # Multi-quantum ($10 to $30 SGD) knapsack arbitrage guide
│   └── optimization_results_summary.json                        # Precomputed benchmark optimizations
├── skills/
│   └── sg-mala-optimiser-engine/
│       └── SKILL.md                                             # Antigravity agent skill specification
├── MASTER_PROMPT_GEMINI_3_8_FLASH.md                             # System master prompt
└── README.md
```

---

## 4. Usage & Execution

### Running the MCP Server
```bash
python mcp_servers/sg_mala_quant_mcp.py
```

### Running Knapsack Solvers Directly in Python
```python
from mcp_servers.sg_mala_quant_mcp import solve_mala_knapsack_30sgd, query_hpb_sgfoodid_recipe_analyser

# Solve $30 Unified Weight margin crusher
res = solve_mala_knapsack_30sgd(budget_sgd=30.0, pricing_model="unified", objective="minimise_restaurant_margin")
print("Wholesale COGS Extracted:", res["total_wholesale_cogs_extracted_sgd"])

# Analyze clinical nutrition for 2 diners
nutr = query_hpb_sgfoodid_recipe_analyser(selected_ingredients=res["allocations"], base_id="B13", diners_count=2)
print("Per-diner sodium (mg):", nutr["per_diner_serving"]["sodium_mg"])
```

---

## 5. Disclaimer

This project is an educational, research, and quantitative operations research simulator for food physics, health policy analysis, and actuarial modeling. It is not intended for clinical decision-making or diagnosis.
