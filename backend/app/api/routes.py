from __future__ import annotations

from app.core.database import SessionLocal
from app.models.material import Material
from app.models.printer import Printer
from app.models.product import Product


def seed_data() -> None:
    db = SessionLocal()
    try:
        if db.query(Printer).count() == 0:
            db.add_all(
                [
                    Printer(
                        name="Bambu Lab X1C",
                        manufacturer="Bambu Lab",
                        model="X1C",
                        build_volume_x=256,
                        build_volume_y=256,
                        build_volume_z=256,
                        available=1,
                        hourly_cost=3.5,
                        location="Workshop A",
                    ),
                    Printer(
                        name="Creality K1 Max",
                        manufacturer="Creality",
                        model="K1 Max",
                        build_volume_x=300,
                        build_volume_y=300,
                        build_volume_z=300,
                        available=1,
                        hourly_cost=2.8,
                        location="Workshop B",
                    ),
                ]
            )

        if db.query(Material).count() == 0:
            db.add_all(
                [
                    Material(
                        brand="Bambu",
                        material_type="PLA",
                        colour="Black",
                        price_per_kg=180,
                        diameter=1.75,
                        available_weight=1000,
                        supplier="Bambu Lab",
                        purchase_date="2026-01-01",
                    ),
                    Material(
                        brand="Prusa",
                        material_type="PLA",
                        colour="White",
                        price_per_kg=150,
                        diameter=1.75,
                        available_weight=500,
                        supplier="Prusa Research",
                        purchase_date="2026-01-15",
                    ),
                ]
            )

        if db.query(Product).count() == 0:
            db.add(
                Product(
                    sku="3D-OPP-001",
                    name="Modular Desk Cable Organizer",
                    slug="modular-desk-cable-organizer",
                    description="A compact desk organization product for cable management.",
                    category="home_office",
                    subcategory="desk_organization",
                    status="DISCOVERED",
                    target_customer="home_office",
                    design_status="prototype",
                    legal_status="CLEAR",
                    market_score=87,
                    demand_score=22,
                    competition_score=11,
                    profit_score=18,
                    print_score=14,
                    personalisation_score=9,
                    trend_score=8,
                    production_score=5,
                    material_cost=24,
                    electricity_cost=2,
                    labour_cost=10,
                    packaging_cost=4,
                    shipping_cost=5,
                    marketplace_fee=12,
                    selling_price=99,
                    estimated_profit=75,
                    actual_profit=0,
                )
            )

        db.commit()
    finally:
        db.close()
