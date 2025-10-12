from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db
from ..models import ConnectedAccount

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("/", response_model=schemas.Account, status_code=status.HTTP_201_CREATED)
def connect_account(payload: schemas.AccountCreate, db: Session = Depends(get_db)):
    property_obj = crud.get_property(db, payload.property_id)
    if not property_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")

    account = crud.create_account(db, payload.dict())
    return account


@router.get("/", response_model=list[schemas.Account])
def list_accounts(property_id: int | None = None, db: Session = Depends(get_db)):
    return crud.list_accounts(db, property_id)


@router.post("/{account_id}/sync", response_model=schemas.Account)
def sync_account(account_id: int, db: Session = Depends(get_db)):
    account = db.query(ConnectedAccount).filter(ConnectedAccount.id == account_id).first()
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")

    account.metadata = account.metadata or {}
    account.metadata.update({"synced": True})
    db.add(account)
    db.commit()
    db.refresh(account)
    return account
