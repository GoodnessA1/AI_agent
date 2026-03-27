#!/bin/python3

from pydantic import BaseModel, Field
from enum import Enum
from uuid import UUID, uuid4

class Gender(Enum):
    Male = 'Male'
    Female = 'Female'


class Person(BaseModel):
    ids: UUID = Field(default_factory=uuid4, frozen = True)
    name: str = Field(min_length = 3)
    age: int
    gender: Gender
