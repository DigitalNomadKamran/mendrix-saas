from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .models import ChannelProvider


class PropertyBase(BaseModel):
    title: str = Field(..., description="Catchy name of the listing")
    description: str
    address: str
    nightly_rate: int = Field(..., ge=0)
    occupancy_rate: Optional[int] = Field(0, ge=0, le=100)


class PropertyCreate(PropertyBase):
    pass


class Property(PropertyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    provider: ChannelProvider
    username: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AccountCreate(AccountBase):
    property_id: int


class Account(AccountBase):
    id: int
    property_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True


class Suggestion(BaseModel):
    id: int
    property_id: int
    summary: str
    details: str
    score: int
    created_at: datetime

    class Config:
        orm_mode = True


class Lead(BaseModel):
    id: int
    property_id: int
    source: str
    contact: str
    message: str
    created_at: datetime

    class Config:
        orm_mode = True


class SuggestionsResponse(BaseModel):
    property: Property
    suggestions: List[Suggestion]


class LeadsResponse(BaseModel):
    property: Property
    leads: List[Lead]
