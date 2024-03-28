from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import Path

class VectorBase(BaseModel):
    description: Optional[str] = None

class VectorCreate(VectorBase):
    name: str = Field(..., example="Vector Name")

class VectorUpdate(VectorBase):
    name: Optional[str] = Field(None, example="New Vector Name")

class Vector(VectorBase):
    id: int
    name: str
    owner_id: int
    class Config:
        orm_mode = True

class TextProcessRequest(BaseModel):
    text: str = Field(..., example="Sample text to process.")
    chunk_size: Optional[int] = Field(default=512, example=512)

class GPTGenerateRequest(BaseModel):
    prompt: str = Field(..., example="Once upon a time,")
    max_length: Optional[int] = Field(default=50, example=50)
    temperature: Optional[float] = Field(default=1.0, example=1.0)


