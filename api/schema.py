import os
from pydantic import BaseModel, Field
from typing import Any, List, Optional

from enum import Enum, auto

class Image(BaseModel):
    file_img: str = Field(examples="base64")
    class Config:
        schema_json_extra = {
            "example" : {
                "file_img": "base64"
            }
        }