from __future__ import annotations

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.material import Material
from app.models.opportunity import ProductOpportunity
from app.models.printer import Printer
from app.models.product import Product
from app.schemas.product import MaterialCreate, OpportunityCreate, PrinterCreate, ProductCreate
from app.services.cost_calculator import calculate_profit, calculate_production_cost
from app.services.scoring_service import score_opportunity

api_router = APIRouter(prefix="/api")


@api_router.get("/health")
def health_route() -> dict[str, str]:
    return {"status": "ok"}


@api_router.get("/opportunities")
def get_opportunities(db: Session = Depends(get_db)):
    items = db.query(ProductOpportunity).order_by(ProductOpportunity.created_at.desc()).all()
    return items


@api_router.post("/opportunities", status_code=status.HTTP_201_CREATED)
def create_opportunity(payload: OpportunityCreate, db: Session = Depends(get_db)):
    item = ProductOpportunity(
        name=payload.name,
        category=payload.category,
        target_customer=payload.target_customer,
        demand=payload.demand,
        competition=payload.competition,
        material_weight_grams=payload.material_weight_grams,
        print_time_hours=payload.print_time_hours,
        selling_price=payload.selling_price,
        notes=payload.notes,
    )

    material_cost = payload.material_weight_grams * 0.18
    production_cost = material_cost + (payload.print_time_hours * 0.08) + 10
    profit = payload.selling_price - production_cost - 8
    score = score_opportunity(85, 70, 80, 82, 75, 78, 88)

    item.material_cost = material_cost
    item.production_cost = production_cost
    item.estimated_profit = profit
    item.opportunity_score = float(score["total"])
    item.status = "ANALYSED"

    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@api_router.get("/printers")
def get_printers(db: Session = Depends(get_db)):
    return db.query(Printer).order_by(Printer.created_at.desc()).all()


@api_router.post("/printers", status_code=status.HTTP_201_CREATED)
def create_printer(payload: PrinterCreate, db: Session = Depends(get_db)):
    item = Printer(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@api_router.get("/materials")
def get_materials(db: Session = Depends(get_db)):
    return db.query(Material).order_by(Material.created_at.desc()).all()


@api_router.post("/materials", status_code=status.HTTP_201_CREATED)
def create_material(payload: MaterialCreate, db: Session = Depends(get_db)):
    item = Material(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@api_router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).order_by(Product.created_at.desc()).all()


@api_router.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    item = Product(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@api_router.post("/costs")
def calculate_cost(payload: dict, db: Session = Depends(get_db)):
    del db
    material_weight_grams = float(payload.get("material_weight_grams", 0))
    material_price_per_gram = float(payload.get("material_price_per_gram", 0.18))
    print_time_hours = float(payload.get("print_time_hours", 0))
    printer_power_kw = float(payload.get("printer_power_kw", 0.15))
    electricity_price_per_kwh = float(payload.get("electricity_price_per_kwh", 1.9))
    labour_cost = float(payload.get("labour_cost", 0))
    failure_percentage = float(payload.get("failure_percentage", 5))
    packaging_cost = float(payload.get("packaging_cost", 0))
    selling_price = float(payload.get("selling_price", 0))
    marketplace_fee = float(payload.get("marketplace_fee", 0))
    shipping_cost = float(payload.get("shipping_cost", 0))

    costs = calculate_production_cost(
        material_weight_grams=material_weight_grams,
        material_price_per_gram=material_price_per_gram,
        print_time_hours=print_time_hours,
        printer_power_kw=printer_power_kw,
        electricity_price_per_kwh=electricity_price_per_kwh,
        labour_cost=labour_cost,
        failure_percentage=failure_percentage,
        packaging_cost=packaging_cost,
    )
    profit = calculate_profit(
        selling_price=selling_price,
        production_cost=costs["production_cost"],
        marketplace_fee=marketplace_fee,
        shipping_cost=shipping_cost,
    )
    return {**costs, **profit}


@api_router.post("/scoring")
def get_score(payload: dict):
    demand = float(payload.get("demand", 80))
    competition = float(payload.get("competition", 60))
    profit = float(payload.get("profit", 75))
    print_suitability = float(payload.get("print_suitability", 82))
    personalisation = float(payload.get("personalisation", 70))
    trend = float(payload.get("trend", 68))
    production = float(payload.get("production", 90))

    return score_opportunity(demand, competition, profit, print_suitability, personalisation, trend, production)


@api_router.get("/dashboard")
def dashboard_summary(db: Session = Depends(get_db)):
    product_count = db.query(Product).count()
    opportunity_count = db.query(ProductOpportunity).count()
    printer_count = db.query(Printer).count()
    material_count = db.query(Material).count()

    return {
        "products": product_count,
        "opportunities": opportunity_count,
        "printers": printer_count,
        "materials": material_count,
    }


class SeedRequest(BaseModel):
    trigger: str = "seed"


@api_router.post("/seed")
def seed_database(payload: SeedRequest, db: Session = Depends(get_db)):
    del payload
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
    return {"status": "seeded"}


__all__ = ["api_router"]
