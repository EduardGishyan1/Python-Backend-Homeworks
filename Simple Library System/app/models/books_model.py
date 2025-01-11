from pydantic import BaseModel, Field
from enum import Enum
from typing import List

class Status(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"

class Books(BaseModel):
    title: str = Field(...,min_length = 3,max_length = 50)
    author: str 
    genre: List[str]
    rating: int = Field(...,min = 0,max = 5)
    pages: int = Field(...,min = 0)
    status:Status