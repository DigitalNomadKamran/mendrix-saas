from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class PropertyListing(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    address = Column(String(255), nullable=False)
    nightly_rate = Column(Integer, nullable=False)
    occupancy_rate = Column(Integer, nullable=True, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    accounts = relationship("ConnectedAccount", back_populates="property")
    suggestions = relationship("OptimizationSuggestion", back_populates="property")
    leads = relationship("Lead", back_populates="property")


class ChannelProvider(str, PyEnum):
    airbnb = "airbnb"
    booking = "booking"


class ConnectedAccount(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    provider = Column(Enum(ChannelProvider), nullable=False)
    username = Column(String(255), nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"))
    metadata = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)

    property = relationship("PropertyListing", back_populates="accounts")


class OptimizationSuggestion(Base):
    __tablename__ = "suggestions"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"))
    summary = Column(String(255), nullable=False)
    details = Column(Text, nullable=False)
    score = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    property = relationship("PropertyListing", back_populates="suggestions")


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"))
    source = Column(String(255), nullable=False)
    contact = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    property = relationship("PropertyListing", back_populates="leads")
