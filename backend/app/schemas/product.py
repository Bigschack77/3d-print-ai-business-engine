from __future__ import annotations

from datetime import datetime

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
