from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from app.core.database import Base


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
