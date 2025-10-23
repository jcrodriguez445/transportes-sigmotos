from pydantic import BaseModel
from typing import Optional

class DestinationBase(BaseModel):
    nombre_ciudad: str
    distancia_km: float
    tiempo_estimado_horas: float
    tarifa_base: float
    punto_partida: Optional[str] = "Bogotá"
    descripcion: Optional[str] = None
    vehicle_id: Optional[int] = None

class DestinationCreate(DestinationBase):
    pass

class DestinationResponse(DestinationBase):
    id: int

    class Config:
        from_attributes = True
