from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from app.core.database import Base


class ProductOpportunity(Base):
    __tablename__ = "product_opportunities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(120), default="home_office")
    target_customer = Column(String(120), default="home_office")
    demand = Column(String(30), default="medium")
    competition = Column(String(30), default="medium")
    material_weight_grams = Column(Float, default=0.0)
    print_time_hours = Column(Float, default=0.0)
    selling_price = Column(Float, default=0.0)
    material_cost = Column(Float, default=0.0)
    production_cost = Column(Float, default=0.0)
    estimated_profit = Column(Float, default=0.0)
    opportunity_score = Column(Float, default=0.0)
    status = Column(String(50), default="DISCOVERED")
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class Printer(Base):
    __tablename__ = "printers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    manufacturer = Column(String(120), default="")
    model = Column(String(120), default="")
    build_volume_x = Column(Float, default=0.0)
    build_volume_y = Column(Float, default=0.0)
    build_volume_z = Column(Float, default=0.0)
    available = Column(Integer, default=1)
    hourly_cost = Column(Float, default=0.0)
    location = Column(String(120), default="")
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(150), nullable=False)
    material_type = Column(String(120), default="PLA")
    colour = Column(String(80), default="Natural")
    price_per_kg = Column(Float, default=0.0)
    diameter = Column(Float, default=1.75)
    available_weight = Column(Float, default=0.0)
    supplier = Column(String(160), default="")
    purchase_date = Column(String(120), default="")
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    @property
    def cost_per_gram(self) -> float:
        if self.price_per_kg <= 0:
            return 0.0
        return self.price_per_kg / 1000.0


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(120), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    description = Column(Text, default="")
    category = Column(String(120), default="home_office")
    subcategory = Column(String(120), default="")
    status = Column(String(80), default="DISCOVERED")
    target_customer = Column(String(120), default="home_office")
    design_status = Column(String(80), default="concept")
    legal_status = Column(String(80), default="CLEAR")
    market_score = Column(Float, default=0.0)
    demand_score = Column(Float, default=0.0)
    competition_score = Column(Float, default=0.0)
    profit_score = Column(Float, default=0.0)
    print_score = Column(Float, default=0.0)
    personalisation_score = Column(Float, default=0.0)
    trend_score = Column(Float, default=0.0)
    production_score = Column(Float, default=0.0)
    material_cost = Column(Float, default=0.0)
    electricity_cost = Column(Float, default=0.0)
    labour_cost = Column(Float, default=0.0)
    packaging_cost = Column(Float, default=0.0)
    shipping_cost = Column(Float, default=0.0)
    marketplace_fee = Column(Float, default=0.0)
    selling_price = Column(Float, default=0.0)
    estimated_profit = Column(Float, default=0.0)
    actual_profit = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
