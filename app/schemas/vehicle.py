from pydantic import BaseModel
from typing import Optional

class VehicleBase(BaseModel):
    placa: str
    modelo: str
    capacidad: int
    estado: Optional[str] = "activo"
    conductor: Optional[str] = None
    observaciones: Optional[str] = None

class VehicleCreate(VehicleBase):
    pass

class VehicleResponse(VehicleBase):
    id: int

    class Config:
        from_attributes = True
