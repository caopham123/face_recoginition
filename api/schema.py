import numpy as np
from pydantic import BaseModel, Field
from typing import Any, List, Optional
from enum import Enum, auto

class Image(BaseModel):
    image: str = Field(examples=["base64"])
    class Config:
        json_schema_extra = {
            "example" : {
                "image": "base64"
            }
        }

class Member(BaseModel):
    email: str = Field(examples="test213@gmail.com")
    name: str
    # embedding: np.array

    class Config:
        json_schema_extra = {
            "example" : {
                "email": "test213@gmail.com",
                "name": "Test Name",
                # "embedding": [0.34, 0.56, 0.78, 0.90]
            }
        }
class UpdateMember(BaseModel):
    email: str = Field(examples="test213@gmail.com")
    name: str
    embedding: str

    class Config:
        json_schema_extra = {
            "example" : {
                "email": "test213@gmail.com",
                "name": "Test Name",
                "embedding": "[0.34, 0.56, 0.78, 0.90]"
            }
        }