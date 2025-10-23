from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.database import Base, engine, SessionLocal
from app.models.vehicle import Vehicle
from app.models.destination import Destination
from app.schemas.vehicle import VehicleCreate, VehicleResponse
from app.schemas.destination import DestinationCreate, DestinationResponse
from app.crud.vehicle import create_vehicle, get_vehicles, get_vehicle, update_vehicle, delete_vehicle
from app.crud.destination import create_destination, get_destinations, get_destination, update_destination, delete_destination

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Transportes Sigmotos API",
    description="Sistema de gestión de rutas y vehículos - Todos los transportes regresan a Bogotá",
    version="1.0.0"
)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Transportes Sigmotos API"}

# ENDPOINTS PARA VEHÍCULOS
@app.post("/vehicles/", response_model=VehicleResponse, tags=["Vehículos"])
def create_vehicle_endpoint(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db=db, vehicle=vehicle)

@app.get("/vehicles/", response_model=list[VehicleResponse], tags=["Vehículos"])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehicles = get_vehicles(db, skip=skip, limit=limit)
    return vehicles

@app.get("/vehicles/{vehicle_id}", response_model=VehicleResponse, tags=["Vehículos"])
def read_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = get_vehicle(db, vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehicle

@app.put("/vehicles/{vehicle_id}", response_model=VehicleResponse, tags=["Vehículos"])
def update_vehicle_endpoint(vehicle_id: int, vehicle: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = update_vehicle(db, vehicle_id, vehicle)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return db_vehicle

@app.delete("/vehicles/{vehicle_id}", tags=["Vehículos"])
def delete_vehicle_endpoint(vehicle_id: int, db: Session = Depends(get_db)):
    success = delete_vehicle(db, vehicle_id)
    if not success:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return {"message": "Vehículo eliminado exitosamente"}

# ENDPOINTS PARA DESTINOS
@app.post("/destinations/", response_model=DestinationResponse, tags=["Destinos"])
def create_destination_endpoint(destination: DestinationCreate, db: Session = Depends(get_db)):
    return create_destination(db=db, destination=destination)

@app.get("/destinations/", response_model=list[DestinationResponse], tags=["Destinos"])
def read_destinations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    destinations = get_destinations(db, skip=skip, limit=limit)
    return destinations

@app.get("/destinations/{destination_id}", response_model=DestinationResponse, tags=["Destinos"])
def read_destination(destination_id: int, db: Session = Depends(get_db)):
    destination = get_destination(db, destination_id)
    if destination is None:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    return destination

@app.put("/destinations/{destination_id}", response_model=DestinationResponse, tags=["Destinos"])
def update_destination_endpoint(destination_id: int, destination: DestinationCreate, db: Session = Depends(get_db)):
    db_destination = update_destination(db, destination_id, destination)
    if db_destination is None:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    return db_destination

@app.delete("/destinations/{destination_id}", tags=["Destinos"])
def delete_destination_endpoint(destination_id: int, db: Session = Depends(get_db)):
    success = delete_destination(db, destination_id)
    if not success:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    return {"message": "Destino eliminado exitosamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
