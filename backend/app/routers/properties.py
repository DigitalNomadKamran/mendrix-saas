from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/properties", tags=["properties"])


@router.post("/", response_model=schemas.Property, status_code=status.HTTP_201_CREATED)
def create_property(payload: schemas.PropertyCreate, db: Session = Depends(get_db)):
    property_obj = crud.create_property(db, payload.dict())
    return property_obj


@router.get("/", response_model=list[schemas.Property])
def list_properties(db: Session = Depends(get_db)):
    return crud.list_properties(db)


@router.get("/{property_id}", response_model=schemas.Property)
def get_property(property_id: int, db: Session = Depends(get_db)):
    property_obj = crud.get_property(db, property_id)
    if not property_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    return property_obj
