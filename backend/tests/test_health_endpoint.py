from backend.app.services.cost_calculator import calculate_production_cost, calculate_profit


def test_calculate_production_cost():
    result = calculate_production_cost(
        material_weight_grams=80,
        material_price_per_gram=0.18,
        print_time_hours=3.2,
        printer_power_kw=0.15,
        electricity_price_per_kwh=1.9,
        labour_cost=10,
        failure_percentage=5,
        packaging_cost=4,
    )

    assert result["material_cost"] > 0
    assert result["production_cost"] > 0


def test_calculate_profit():
    result = calculate_profit(selling_price=99, production_cost=24, marketplace_fee=10, shipping_cost=5)
    assert result["profit"] == 60.0
    assert result["gross_margin"] > 0
