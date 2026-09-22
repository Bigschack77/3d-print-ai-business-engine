from __future__ import annotations

from math import isfinite


def score_opportunity(
    demand: float,
    competition: float,
    profit: float,
    print_suitability: float,
    personalisation: float,
    trend: float,
    production: float,
) -> dict:
    demand_score = min(max(demand, 0), 100) * 0.25
    competition_score = min(max(competition, 0), 100) * 0.15
    profit_score = min(max(profit, 0), 100) * 0.20
    print_score = min(max(print_suitability, 0), 100) * 0.15
    personalisation_score = min(max(personalisation, 0), 100) * 0.10
    trend_score = min(max(trend, 0), 100) * 0.10
    production_score = min(max(production, 0), 100) * 0.05

    total = (
        demand_score
        + competition_score
        + profit_score
        + print_score
        + personalisation_score
        + trend_score
        + production_score
    )

    return {
        "demand": round(demand_score, 2),
        "competition": round(competition_score, 2),
        "profit": round(profit_score, 2),
        "print_suitability": round(print_score, 2),
        "personalisation": round(personalisation_score, 2),
        "trend": round(trend_score, 2),
        "production": round(production_score, 2),
        "total": round(total, 2),
    }


def convert_to_100_scale(value: float) -> float:
    if not isfinite(value):
        return 0.0
    return max(0.0, min(100.0, value))
