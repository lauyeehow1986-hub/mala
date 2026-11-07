# Singapore Mala: Mediterranean Diet × HPB Healthier Dining Programme (HDP) Optimization Report

## Executive Summary
This report details the mathematical formulation, clinical food-physics simulation, and sensory flavor architecture of the optimal **$\$30.00$ SGD Mediterranean Diet × Singapore Health Promotion Board (HPB) My Healthy Plate** Mala bowl.

Utilizing the `sg-mala-quant-mcp` simulator, HPB Singapore Food Insights Database (SG FoodID) Recipe Analyser, and Cellular Sheaf Hypergraph Laplacian engine, we evaluate:
1. Exact ingredient selection across 10 categories balancing marine Omega-3 fatty acids, soy phyto-proteins, high-sulforaphane cruciferous greens, fungal beta-glucans, and unrefined slow starches.
2. The food physics of **Dry Stir-Fry (Mala Xiang Guo)** vs. **Dry Toss (Mala Ban)** vs. **Soup Malatang** accounting for actual diner ingestion fractions ($\phi_{\text{ingest}}$).
3. The 14 broth and sauce bases (`B01` to `B14`), distinguishing capsaicin benefits from saturated fat-carrier hazards (beef tallow / palm oil), hidden sugar traps, and sodium hyper-concentration.
4. The **Mediterranean Flavor Alchemy Protocol** achieving peak sensory hedonics (50Hz green Sichuan peppercorn sanshool tingling, Chinkiang vinegar acid-salt enhancement, allium umami) with minimal caloric/sodium burden.

---

## 1. Optimal $30.00 SGD Mediterranean × HPB Basket

Under Unified Weight pricing ($\$2.98/100\text{g}$, standard at *Yang Guo Fu, Zhang Liang, Gong Yuan, A Hot Hideout*), $\$30.00$ purchases **$1,006.7\text{g}$** of raw ingredients (shared across 2 diners at $\$15.00/\text{pax}$):

| Category | Ingredient | Scale Weight | Protein | Fiber | Saturated Fat | Sodium | Clinical Mechanism |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Marine Seafood** | Barramundi / Seabass Fillet | $150.0\text{g}$ | $28.8\text{g}$ | $0.0\text{g}$ | $0.98\text{g}$ | $87\text{mg}$ | High marine Omega-3 EPA/DHA; cardioprotective. |
| **Marine Seafood** | Deshelled Vannamei Prawns | $80.0\text{g}$ | $16.1\text{g}$ | $0.0\text{g}$ | $0.20\text{g}$ | $132\text{mg}$ | Dense astaxanthin antioxidant; zero saturated fat. |
| **Marine Seafood** | Squid Flower Cut / Sotong | $70.0\text{g}$ | $10.9\text{g}$ | $0.0\text{g}$ | $0.25\text{g}$ | $31\text{mg}$ | Rich in taurine and copper; low cholesterol density. |
| **Soy & Legume** | Tau Kwa (Firm Pressed Tofu) | $150.0\text{g}$ | $23.7\text{g}$ | $1.8\text{g}$ | $1.95\text{g}$ | $21\text{mg}$ | Non-fried plant isoflavones; cardioprotective sterols. |
| **Cruciferous** | Fresh Broccoli Florets | $130.0\text{g}$ | $3.6\text{g}$ | $3.4\text{g}$ | $0.05\text{g}$ | $43\text{mg}$ | Glucoraphanin & sulforaphane; phase-II liver detox. |
| **Leafy Greens** | Xiao Bai Cai (Bok Choy) | $100.0\text{g}$ | $1.5\text{g}$ | $1.0\text{g}$ | $0.03\text{g}$ | $65\text{mg}$ | High potassium (counteracts sodium) & bioavailable folate. |
| **Bioactive Fungi**| King Oyster Mushroom (Eryngii)| $100.0\text{g}$ | $3.3\text{g}$ | $3.4\text{g}$ | $0.06\text{g}$ | $9\text{mg}$ | Ergothioneine & beta-glucans; savory nucleotide umami. |
| **Medicinal Fungi**| Black Wood Ear (Mu Er) | $76.7\text{g}$ | $0.8\text{g}$ | $5.4\text{g}$ | $0.02\text{g}$ | $6\text{mg}$ | Soluble gut mucilage; lowers LDL cholesterol. |
| **Slow Starch** | Konjac Shirataki Knots | $50.0\text{g}$ | $0.1\text{g}$ | $1.4\text{g}$ | $0.01\text{g}$ | $4\text{mg}$ | Zero-glycemic glucomannan; prebiotic gut fermentation. |
| **Sea Vegetable** | Kelp Knots (Hai Dai) | $100.0\text{g}$ | $1.2\text{g}$ | $2.8\text{g}$ | $0.05\text{g}$ | $120\text{mg}$ | Alginate & organic iodine; supports metabolic rate. |
| **Total Basket** | **Raw Ingredients Only** | **$1,006.7\text{g}$** | **$90.0\text{g}$** | **$19.2\text{g}$** | **$3.65\text{g}$** | **$518\text{mg}$** | **Per Diner (2 pax): $45.0\text{g}$ Protein, $9.6\text{g}$ Fiber!** |

---

## 2. Format Showdown: Ingestion Fractions & Food Physics

$$\text{Ingested Lipid/Sodium} = \sum_{i} w_i \cdot \text{Nutrient}_i + \phi_{\text{ingest}}(b) \cdot \text{Nutrient}_{\text{base}}(b)$$

1. **Dry Stir-Fry (Mala Xiang Guo — Bases `B01`–`B04`)**:
   - $\phi_{\text{ingest}} = 1.0$: $100\%$ of the wok-adhered oil, tallow, and paste is ingested.
   - High-temperature wok frying ($>180^\circ\text{C}$) triggers lipid peroxidation and advanced glycation end-products (AGEs).
   - At *Te La* (`B01`), saturated fat reaches **$12.94\text{g}$ per diner**, breaching HPB HDP safety ceilings.
   - *Mitigation*: Diners must order `B05` (*Shao You, Shao Yan, Wei La*), which reduces added lipid by $61\%$.
2. **Dry Toss (Mala Ban — Base `B08`)**:
   - $\phi_{\text{ingest}} = 1.0$, but blanched in clean boiling water first, rendering out excess fats and surface starches.
   - Dressed with roasted sesame paste (tahini equivalent — high MUFAs and sesamin lignans), aged Chinkiang vinegar, and light Sichuan peppercorn oil.
   - Total saturated fat is restricted to **$3.39\text{g}$**, with $876\text{mg}$ sodium.
3. **Soup Malatang (Bases `B09`–`B13`)**:
   - **The Broth Dilution & Ingestion Shield**: The aqueous broth acts as a flavor extraction bath. Typical soup consumption is only **$35\%\text{--}40\%$** ($\phi_{\text{ingest}} = 0.35\text{--}0.40$).
   - By leaving the residual soup unconsumed, ingested sodium drops from pot-level $2,650\text{mg}$ down to **$490\text{--}670\text{mg}$ per diner**, effortlessly satisfying HPB guidelines ($\le 1,000\text{mg}$).

---

## 3. Simulation Scorecard Across 8 Broth Bases (Per Diner, 2 Pax Sharing)

| Base ID | Base Name | Category | $\phi_{\text{ingest}}$ | Kcal | Protein | Fiber | Sat Fat | Ingested Sodium | HPB HDP Compliance | Nutri-Grade |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`B01`** | Dry Te La (Extra Spicy) | Dry Stir-Fry | $1.00$ | $605\text{ kcal}$ | $47.5\text{g}$ | $7.9\text{g}$ | **$12.94\text{g}$** | $1,431\text{mg}$ ($72\%$) | ❌ **FAIL** (Sat Fat > 10g) | **Grade D** |
| **`B03`** | Dry Zhong La (Medium Spicy) | Dry Stir-Fry | $1.00$ | $480\text{ kcal}$ | $46.8\text{g}$ | $7.4\text{g}$ | **$7.79\text{g}$** | $1,066\text{mg}$ ($53\%$) | ⚠️ Borderline (Sodium) | **Grade C** |
| **`B05`** | Dry Shao You Shao Yan Wei La | Dry Stir-Fry | $1.00$ | $377\text{ kcal}$ | $46.2\text{g}$ | $7.1\text{g}$ | **$3.09\text{g}$** | $596\text{mg}$ ($30\%$) | ✅ **PASS** | **Grade B** |
| **`B08`** | Dry Toss Mala Ban | Dry Toss | $1.00$ | $447\text{ kcal}$ | $48.3\text{g}$ | $7.6\text{g}$ | **$3.39\text{g}$** | $876\text{mg}$ ($44\%$) | ✅ **PASS** | **Grade B** |
| **`B09`** | Soup Classic Beef Tallow | Soup Malatang| $0.35$ | $406\text{ kcal}$ | $46.2\text{g}$ | $6.9\text{g}$ | **$5.89\text{g}$** | $766\text{mg}$ ($38\%$) | ✅ **PASS** | **Grade C** |
| **`B10`** | Soup Spicy Pork Collagen | Soup Malatang| $0.35$ | $383\text{ kcal}$ | $47.1\text{g}$ | $6.8\text{g}$ | **$4.05\text{g}$** | $670\text{mg}$ ($34\%$) | ✅ **PASS** | **Grade B** |
| **`B11`** | **Soup Rich Tomato & Pepper**| Soup Malatang| $0.45$ | **$352\text{ kcal}$**| **$46.3\text{g}$**| **$7.2\text{g}$** | **$2.05\text{g}$** | **$600\text{mg}$ ($30\%$)** | ✅ **BEST DUO (Lycopene)** | **Grade A** |
| **`B13`** | **Soup Wild Mushroom & Herb**| Soup Malatang| $0.40$ | **$334\text{ kcal}$**| **$46.3\text{g}$**| **$6.9\text{g}$** | **$1.81\text{g}$** | **$490\text{mg}$ ($25\%$)** | ✅ **CLEANEST (Beta-Glucan)**| **Grade A** |

---

## 4. Spiciness vs. Non-Spicy Health Pitfalls

1. **The Capsaicin-Fat Carrier Trap**: Capsaicin is a lipophilic alkaloid. In commercial kitchens, stalls dissolve capsaicin into heavy beef tallow or palm olein. Ordering *Da La* or *Te La* results in 2–3 additional ladles of saturated oil ($+20\text{--}40\text{g}$ lipid).
2. **Hidden Sugars**: Low-grade tomato broths and sweet Mala Ban dressings add $15\text{--}25\text{g}$ of sucrose or fructose corn syrup to mask harsh chili seeds and excessive salt.
3. **Acute Sodium Spikes**: Pixian *doubanjiang*, *douchi*, and MSG concentrate sodium to $>3,000\text{mg}$ in full-pot spicy broths. Drinking the entire soup bowl causes acute vascular resistance and water retention.

---

## 5. The Mediterranean Flavor Alchemy Protocol

To ensure extraordinary flavor without the caloric or sodium penalty:
- **Base Choice**: Select `B11` (Rich Tomato) or `B13` (Wild Mushroom). Natural glutamates and guanylates provide deep savory richness.
- **Teng Jiao You (Green Sichuan Pepper Oil)**: 1 tsp delivers pure *hydroxy-alpha-sanshool* (50Hz lingual mechanoreceptor vibration) with near-zero calories.
- **Aged Chinkiang Black Vinegar**: Acetic acid blunts postprandial glucose spikes by $20\text{--}30\%$ and cross-modally amplifies saltiness, making low-sodium broths taste punchy.
- **Fresh Alliums & Chilies**: Minced raw garlic (allicin) and fresh sliced bird's eye chilies provide pure capsaicin without saturated fat carriers.
- **The Golden Rule**: Eat all solid ingredients; leave $60\%\text{--}70\%$ of the liquid broth unconsumed.
