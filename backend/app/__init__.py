from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from app.core.database import Base


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
