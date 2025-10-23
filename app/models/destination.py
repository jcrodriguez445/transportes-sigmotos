from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    nombre_ciudad = Column(String(100), nullable=False)
    distancia_km = Column(Float, nullable=False)
    tiempo_estimado_horas = Column(Float, nullable=False)
    tarifa_base = Column(Float, nullable=False)
    punto_partida = Column(String(100), default="Bogotá")
    descripcion = Column(Text)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    
    # Relación
    vehicle = relationship("Vehicle")
