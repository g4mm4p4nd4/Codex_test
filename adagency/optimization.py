from typing import Dict


def recommend_budget(performance: Dict[str, float]) -> Dict[str, float]:
    """Recommend budget allocation based on conversion rates."""
    total = sum(performance.values()) or 1.0
    return {campaign: value / total for campaign, value in performance.items()}
