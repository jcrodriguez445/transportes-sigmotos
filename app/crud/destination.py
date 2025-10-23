from sqlalchemy.orm import Session
from app.models.destination import Destination
from app.schemas.destination import DestinationCreate

def create_destination(db: Session, destination: DestinationCreate):
    db_destination = Destination(**destination.model_dump())
    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)
    return db_destination

def get_destinations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Destination).offset(skip).limit(limit).all()

def get_destination(db: Session, destination_id: int):
    return db.query(Destination).filter(Destination.id == destination_id).first()

def update_destination(db: Session, destination_id: int, destination: DestinationCreate):
    db_destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if db_destination:
        for key, value in destination.model_dump().items():
            setattr(db_destination, key, value)
        db.commit()
        db.refresh(db_destination)
    return db_destination

def delete_destination(db: Session, destination_id: int):
    db_destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if db_destination:
        db.delete(db_destination)
        db.commit()
        return True
    return False
