from __future__ import annotations


def calculate_material_cost(material_weight_grams: float, material_price_per_gram: float) -> float:
    return material_weight_grams * material_price_per_gram


def calculate_electricity_cost(
    print_time_hours: float,
    printer_power_kw: float,
    electricity_price_per_kwh: float,
) -> float:
    return print_time_hours * printer_power_kw * electricity_price_per_kwh


def calculate_production_cost(
    material_weight_grams: float,
    material_price_per_gram: float,
    print_time_hours: float,
    printer_power_kw: float,
    electricity_price_per_kwh: float,
    labour_cost: float,
    failure_percentage: float,
    packaging_cost: float,
) -> dict:
    material_cost = calculate_material_cost(material_weight_grams, material_price_per_gram)
    electricity_cost = calculate_electricity_cost(print_time_hours, printer_power_kw, electricity_price_per_kwh)
    failure_allowance = material_cost * (failure_percentage / 100.0)
    production_cost = material_cost + electricity_cost + labour_cost + failure_allowance + packaging_cost

    return {
        "material_cost": round(material_cost, 2),
        "electricity_cost": round(electricity_cost, 2),
        "failure_allowance": round(failure_allowance, 2),
        "production_cost": round(production_cost, 2),
    }


def calculate_profit(
    selling_price: float,
    production_cost: float,
    marketplace_fee: float,
    shipping_cost: float,
) -> dict:
    profit = selling_price - production_cost - marketplace_fee - shipping_cost
    gross_margin = (profit / selling_price) if selling_price else 0.0

    return {
        "profit": round(profit, 2),
        "gross_margin": round(gross_margin, 4),
    }
