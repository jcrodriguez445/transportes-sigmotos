from sqlalchemy import Column, Integer, String, Text
from app.models.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10), unique=True, index=True, nullable=False)
    modelo = Column(String(50), nullable=False)
    capacidad = Column(Integer, nullable=False)
    estado = Column(String(20), default="activo")
    conductor = Column(String(100))
    observaciones = Column(Text)
