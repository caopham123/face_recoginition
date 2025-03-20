import os
from pydantic import BaseModel, Field
from typing import Any, List, Optional
import uuid
from enum import Enum, auto

class Image(BaseModel):
    image: str = Field(examples=["base64"])
    class Config:
        json_schema_extra = {
            "example" : {
                "image": "base64"
            }
        }

class Test(BaseModel):
    img: str

class Member(BaseModel):
    email: str = Field(examples="test213@gmail.com")
    name: str
    class Config:
        json_schema_extra = {
            "example" : {
                "email": "test213@gmail.com",
                "name": "Test Name"
            }
        }