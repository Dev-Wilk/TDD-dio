import datetime
from pydantic import BaseModel, Field
from uuid import UUID4


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    class Config:
        from_attributes = True
