"""User models for PawPal Composite Service."""
from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class User(BaseModel):
    """User representation."""
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    rating: Optional[float] = None
    total_reviews: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class Dog(BaseModel):
    """Dog representation."""
    id: Optional[str] = None
    owner_id: Optional[str] = None
    name: Optional[str] = None
    breed: Optional[str] = None
    age: Optional[int] = None
    size: Optional[str] = None
    temperament: Optional[str] = None
    energy_level: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

