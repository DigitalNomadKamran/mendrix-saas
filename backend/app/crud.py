from __future__ import annotations
from typing import Dict, Iterable, List, Sequence

from sqlalchemy.orm import Session

from .models import ChannelProvider, ConnectedAccount, Lead, OptimizationSuggestion, PropertyListing


def create_property(db: Session, payload: Dict) -> PropertyListing:
    property_obj = PropertyListing(**payload)
    db.add(property_obj)
    db.commit()
    db.refresh(property_obj)
    return property_obj


def list_properties(db: Session) -> Sequence[PropertyListing]:
    return db.query(PropertyListing).order_by(PropertyListing.created_at.desc()).all()


def get_property(db: Session, property_id: int) -> PropertyListing | None:
    return db.query(PropertyListing).filter(PropertyListing.id == property_id).first()


def create_account(db: Session, payload: Dict) -> ConnectedAccount:
    account = ConnectedAccount(**payload)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


def list_accounts(db: Session, property_id: int | None = None) -> Sequence[ConnectedAccount]:
    query = db.query(ConnectedAccount)
    if property_id:
        query = query.filter(ConnectedAccount.property_id == property_id)
    return query.order_by(ConnectedAccount.created_at.desc()).all()


def create_suggestions(db: Session, property_id: int, items: Iterable[Dict]) -> List[OptimizationSuggestion]:
    suggestions = [OptimizationSuggestion(property_id=property_id, **item) for item in items]
    db.add_all(suggestions)
    db.commit()
    for suggestion in suggestions:
        db.refresh(suggestion)
    return suggestions


def list_suggestions(db: Session, property_id: int) -> Sequence[OptimizationSuggestion]:
    return (
        db.query(OptimizationSuggestion)
        .filter(OptimizationSuggestion.property_id == property_id)
        .order_by(OptimizationSuggestion.created_at.desc())
        .all()
    )


def create_leads(db: Session, property_id: int, items: Iterable[Dict]) -> List[Lead]:
    leads = [Lead(property_id=property_id, **item) for item in items]
    db.add_all(leads)
    db.commit()
    for lead in leads:
        db.refresh(lead)
    return leads


def list_leads(db: Session, property_id: int) -> Sequence[Lead]:
    return (
        db.query(Lead)
        .filter(Lead.property_id == property_id)
        .order_by(Lead.created_at.desc())
        .all()
    )


def provider_from_string(value: str) -> ChannelProvider:
    try:
        return ChannelProvider(value)
    except ValueError as exc:
        raise ValueError(f"Unsupported provider: {value}") from exc
