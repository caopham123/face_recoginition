import numpy as np
from pydantic import BaseModel, Field
from typing import Any, List, Optional
from enum import Enum, auto
import uuid

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
    embedding: Optional[str] = None
    image: Optional[str] = None
    member_id: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example" : {
                "email": "test213@gmail.com",
                "name": "Test Name",
                "embedding": "0.34, 0.56, 0.78, 0.90",
                "member_id": "53445ba0-7a1f-41db-9b2d-7716b2c9c27b"
            }
        }

class UpdateMember(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    embedding: Optional[str] = None
    image: Optional[str] = None
    member_id: str = Field(examples="53445ba0-80af24802")

    # class Config:
    #     json_schema_extra = {
    #         "example" : {
    #             "email": "test213@gmail.com",
    #             "name": "Test Name",
    #             "embedding": "0.34, 0.56, 0.78, 0.90",
    #             "member_id": "53445ba0-7a1f-41db-9b2d-7716b2c9c27b"
    #         }
    #     }