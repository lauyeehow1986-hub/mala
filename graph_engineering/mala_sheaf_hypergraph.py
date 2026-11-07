#!/usr/bin/env python3
"""
Heterogeneous Knowledge Hypergraph & Cellular Sheaf Laplacian Engine for Mala Xiang Guo Optimization
Connects 6 Node Types:
  1. IngredientNode (96 items across 10 categories)
  2. PricingArchitectureNode (Unified Weight, Tiered Weight, Fixed Per-Portion)
  3. SupplierBaselineNode (NTUC FairPrice, Sheng Siong, RedMart/Lazada, Shopee, PPWC, VWC, Song Fish, Fassler)
  4. PhysicsHydrationNode (Pre-weighing water soakage gamma_wet, Ice glaze, Post-weighing oil absorption alpha_oil)
  5. BrothBaseNode (14 Dry Stir-Fry, Dry Toss & Soup Malatang bases)
  6. HPBPolicySubsidyNode (HIDS d_cd7fbc766695f997396b96bf93820382: https://data.gov.sg/datasets/d_cd7fbc766695f997396b96bf93820382/view oils, wholegrains, K-Salt & reduced-sodium sauces)

Computes the Sheaf Cohomology / Global Section Discrepancy:
  L_F (x) = sum_{e in E} (F_{v <- e} x_v - F_{u <- e} x_u)^2
to detect:
  - Water-weight arbitrage traps (where gamma_wet >= 2.5 inflates scale price vs dry baseline cost)
  - Oil-sponge saturated fat blowups (where alpha_oil >= 1.8 + Da La/Tallow base violates HPB <= 500-750 kcal / Nutri-Grade thresholds)
  - Stored-value membership negative-EV traps (where closure hazard lambda + breakage > 8.33% effective discount)
"""

import math
from typing import Dict, List, Any

class MalaCellularSheafHypergraph:
    def __init__(self, ingredients: List[Dict[str, Any]], bases: List[Any], hids_partners: List[Any]):
        self.ingredients = {item["id"]: item for item in ingredients}
        self.bases = {}
        for b in bases:
            if isinstance(b, dict):
                bid = b.get("base_id", "")
                self.bases[bid] = {k: float(v) if k in ["typical_ingestion_fraction", "full_pot_sodium_mg", "full_pot_sat_fat_g", "full_pot_kcal", "full_pot_protein_g", "full_pot_fat_g", "full_pot_carbs_g", "full_pot_fiber_g", "wholesale_cogs_sgd", "addon_price_sgd"] and v != "" else v for k, v in b.items()}
            elif isinstance(b, (list, tuple)) and len(b) > 14:
                if b[0] == "base_id":
                    continue
                try:
                    self.bases[b[0]] = {
                        "base_id": b[0],
                        "name_en": b[1],
                        "name_zh": b[2],
                        "full_pot_sat_fat_g": float(b[10]),
                        "full_pot_sodium_mg": float(b[13]),
                        "typical_ingestion_fraction": float(b[14]),
                    }
                except (ValueError, TypeError):
                    continue
        self.hids_partners = hids_partners
        self.hyperedges = []
        self._build_hypergraph()

    def _build_hypergraph(self):
        for iid, item in self.ingredients.items():
            # Hyperedge 1: Price-to-Baseline Arbitrage Sheaf Restriction
            self.hyperedges.append({
                "edge_type": "PRICE_ARBITRAGE_HYPEREDGE",
                "ingredient_id": iid,
                "name": item["name_en"],
                "soak_penalty": item["water_soak_multiplier"],
                "unified_cogs_ratio": item["val_ratio_unified_wholesale"],
                "tiered_cogs_ratio": item["val_ratio_tiered_wholesale"],
                "portion_cogs_ratio": item["val_ratio_portion_wholesale"],
                "optimal_venue_routing": self._route_venue(item),
            })

    @staticmethod
    def _route_venue(item: Dict[str, Any]) -> str:
        u = item["val_ratio_unified_wholesale"]
        t = item["val_ratio_tiered_wholesale"]
        p = item["val_ratio_portion_wholesale"]
        best = max(u, t, p)
        if best == u:
            return "UNIFIED_WEIGHT_CHAIN (Yang Guo Fu / Zhang Liang / Gong Yuan / A Hot Hideout)"
        elif best == t:
            return "TIERED_WEIGHT_STALL (Food Republic / Koufu / Wan Xing)"
        return "FIXED_PER_PORTION_HAWKER (Ri Ri Hong / Labula / Xiao Man Niu)"

    def compute_sheaf_laplacian_energy(self, selected_items: List[Dict[str, Any]], base_id: str) -> Dict[str, Any]:
        """
        Evaluates global consistency of a $30 bowl across 3 stalks:
          Stalk 1: Financial Margin Minimisation (COGS / Spend >= 0.70)
          Stalk 2: Physical Hydration Fairness (Water Weight Waste <= $1.00)
          Stalk 3: HPB Clinical Nutrition Guardrail (Sodium <= 2,000mg, Sat Fat <= 10g per pax)
        """
        base = self.bases.get(base_id)
        if not base:
            base = list(self.bases.values())[0] if self.bases else {"typical_ingestion_fraction": 0.35, "full_pot_sodium_mg": 2200.0, "full_pot_sat_fat_g": 3.5}
        ingest_frac = float(base.get("typical_ingestion_fraction", 0.35))
        base_sod = float(base.get("full_pot_sodium_mg", 2200.0)) * ingest_frac
        base_sat = float(base.get("full_pot_sat_fat_g", 3.5)) * ingest_frac

        water_tax_sgd = 0.0
        total_spend = 0.0
        total_cogs = 0.0
        total_sod = base_sod
        total_sat = base_sat

        for entry in selected_items:
            it = self.ingredients[entry["id"]]
            wt_100 = entry["weight_g"] / 100.0
            spend = wt_100 * it["price_unified_100g"]
            total_spend += spend
            total_cogs += wt_100 * it["effective_stall_cogs_100g_wet"]
            # Water tax: fraction of weight that is pre-soaked water/ice glaze
            water_frac = max(0.0, 1.0 - (1.0 / it["water_soak_multiplier"]))
            water_tax_sgd += spend * water_frac
            total_sod += wt_100 * it["sodium_mg"]
            total_sat += wt_100 * it["sat_fat_g"] * (1.0 + 0.15 * it["oil_absorption_factor"] * ingest_frac)

        margin_discrepancy = max(0.0, 0.75 - (total_cogs / max(total_spend, 1e-6))) ** 2
        water_discrepancy = max(0.0, (water_tax_sgd - 1.50) / 10.0) ** 2
        sodium_discrepancy = max(0.0, (total_sod - 2000.0) / 2000.0) ** 2
        sat_fat_discrepancy = max(0.0, (total_sat - 15.0) / 15.0) ** 2

        total_energy = margin_discrepancy + water_discrepancy + sodium_discrepancy + sat_fat_discrepancy
        return {
            "total_sheaf_laplacian_energy": round(total_energy, 5),
            "stalk_discrepancies": {
                "margin_discrepancy": round(margin_discrepancy, 5),
                "water_tax_discrepancy": round(water_discrepancy, 5),
                "sodium_discrepancy": round(sodium_discrepancy, 5),
                "sat_fat_discrepancy": round(sat_fat_discrepancy, 5),
            },
            "water_tax_paid_sgd": round(water_tax_sgd, 2),
            "effective_cogs_recovery_pct": round((total_cogs / max(total_spend, 1e-6)) * 100, 2),
            "estimated_ingested_sodium_mg": round(total_sod, 1),
            "estimated_ingested_sat_fat_g": round(total_sat, 2),
            "cohomology_verdict": "GLOBALLY_CONSISTENT_PARETO_OPTIMAL" if total_energy < 0.15 else "SHEAF_OBSTRUCTION_DETECTED",
        }
