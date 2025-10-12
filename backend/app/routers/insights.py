from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db
from ..services import generate_leads, generate_suggestions

router = APIRouter(prefix="/insights", tags=["insights"])


@router.get("/{property_id}/suggestions", response_model=schemas.SuggestionsResponse)
def property_suggestions(property_id: int, db: Session = Depends(get_db)):
    property_obj = crud.get_property(db, property_id)
    if not property_obj:
        raise HTTPException(status_code=404, detail="Property not found")

    existing = crud.list_suggestions(db, property_id)
    if not existing:
        suggestions = generate_suggestions(property_obj)
        crud.create_suggestions(
            db,
            property_id,
            [
                {
                    "summary": suggestion.summary,
                    "details": suggestion.details,
                    "score": suggestion.score,
                }
                for suggestion in suggestions
            ],
        )
        existing = crud.list_suggestions(db, property_id)

    return schemas.SuggestionsResponse(property=property_obj, suggestions=existing)


@router.get("/{property_id}/leads", response_model=schemas.LeadsResponse)
def property_leads(property_id: int, db: Session = Depends(get_db)):
    property_obj = crud.get_property(db, property_id)
    if not property_obj:
        raise HTTPException(status_code=404, detail="Property not found")

    existing = crud.list_leads(db, property_id)
    if not existing:
        leads = generate_leads(property_obj)
        crud.create_leads(
            db,
            property_id,
            [
                {
                    "source": lead.source,
                    "contact": lead.contact,
                    "message": lead.message,
                }
                for lead in leads
            ],
        )
        existing = crud.list_leads(db, property_id)

    return schemas.LeadsResponse(property=property_obj, leads=existing)
