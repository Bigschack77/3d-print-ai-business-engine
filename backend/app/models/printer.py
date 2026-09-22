from __future__ import annotations

from app.core.database import Base
from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from datetime import datetime


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
