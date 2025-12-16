"""Review models for PawPal Composite Service."""
from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class ReviewCreate(BaseModel):
    """Payload for creating a new review."""
    walkId: str = Field(..., description="ID of the associated walk")
    ownerId: str = Field(..., description="ID of the dog owner who wrote the review")
    walkerId: str = Field(..., description="ID of the walker being reviewed")
    rating: float = Field(..., ge=1.0, le=5.0, description="Rating from 1.0 to 5.0")
    comment: Optional[str] = Field(None, description="Review comment")

class ReviewUpdate(BaseModel):
    """Payload for updating a review."""
    rating: Optional[float] = Field(None, ge=1.0, le=5.0, description="Updated rating")
    comment: Optional[str] = Field(None, description="Updated comment")

class Review(BaseModel):
    """Review representation."""
    id: str = Field(..., description="Unique review identifier")
    walkId: str = Field(..., description="ID of the associated walk")
    ownerId: str = Field(..., description="ID of the dog owner who wrote the review")
    walkerId: str = Field(..., description="ID of the walker being reviewed")
    rating: float = Field(..., ge=1.0, le=5.0, description="Rating from 1.0 to 5.0")
    comment: Optional[str] = Field(None, description="Review comment")
    createdAt: datetime = Field(..., description="Timestamp when review was created")
    updatedAt: datetime = Field(..., description="Timestamp when review was last updated")


