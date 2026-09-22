from __future__ import annotations

from pydantic import BaseModel


class OpportunityCreate(BaseModel):
    name: str
    category: str = "home_office"
    target_customer: str = "home_office"
    demand: str = "medium"
    competition: str = "medium"
    material_weight_grams: float = 0.0
    print_time_hours: float = 0.0
    selling_price: float = 0.0
    notes: str = ""


class ProductCreate(BaseModel):
    sku: str
    name: str
    slug: str
    description: str = ""
    category: str = "home_office"
    subcategory: str = ""
    status: str = "DISCOVERED"
    target_customer: str = "home_office"
    design_status: str = "concept"
    legal_status: str = "CLEAR"
    market_score: float = 0.0
    demand_score: float = 0.0
    competition_score: float = 0.0
    profit_score: float = 0.0
    print_score: float = 0.0
    personalisation_score: float = 0.0
    trend_score: float = 0.0
    production_score: float = 0.0
    material_cost: float = 0.0
    electricity_cost: float = 0.0
    labour_cost: float = 0.0
    packaging_cost: float = 0.0
    shipping_cost: float = 0.0
    marketplace_fee: float = 0.0
    selling_price: float = 0.0
    estimated_profit: float = 0.0
    actual_profit: float = 0.0


class MaterialCreate(BaseModel):
    brand: str
    material_type: str = "PLA"
    colour: str = "Natural"
    price_per_kg: float = 0.0
    diameter: float = 1.75
    available_weight: float = 0.0
    supplier: str = ""
    purchase_date: str = ""
    notes: str = ""


class PrinterCreate(BaseModel):
    name: str
    manufacturer: str = ""
    model: str = ""
    build_volume_x: float = 0.0
    build_volume_y: float = 0.0
    build_volume_z: float = 0.0
    available: int = 1
    hourly_cost: float = 0.0
    location: str = ""
    notes: str = ""
