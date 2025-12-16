"""Walk models - reused from Walk Service."""
from __future__ import annotations
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field

class WalkBase(BaseModel):
    """Core attributes of a scheduled dog walk."""
    owner_id: UUID = Field(
        ...,
        description="Unique ID of the dog owner requesting the walk.",
        json_schema_extra={"example": "11111111-1111-4111-8111-111111111111"},
    )
    pet_id: UUID = Field(
        ...,
        description="Unique ID of the pet to be walked.",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    location: str = Field(
        ...,
        description="Exact walking start location (street or park).",
        json_schema_extra={"example": "123 Riverside Park, NY"},
    )
    city: str = Field(
        ...,
        description="City where the walk occurs.",
        json_schema_extra={"example": "New York"},
    )
    scheduled_time: datetime = Field(
        ...,
        description="Planned start time (ISO 8601 UTC).",
        json_schema_extra={"example": "2025-10-12T14:30:00Z"},
    )
    duration_minutes: int = Field(
        ...,
        description="Expected walk duration, in minutes.",
        json_schema_extra={"example": 30},
    )
    status: str = Field(
        default="requested",
        description="Walk status: requested, accepted, completed, cancelled.",
        json_schema_extra={"example": "requested"},
    )

class WalkCreate(WalkBase):
    """Payload for creating a new walk request."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated walk ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )

class WalkUpdate(BaseModel):
    """Partial update for an existing walk."""
    scheduled_time: Optional[datetime] = Field(None, description="New scheduled start time.")
    duration_minutes: Optional[int] = Field(None, description="New duration (minutes).")
    location: Optional[str] = Field(None, description="Updated walk location.")
    city: Optional[str] = Field(None, description="Updated walk city.")
    status: Optional[str] = Field(None, description="Walk status.")

class WalkRead(WalkBase):
    """Server representation returned to clients."""
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

