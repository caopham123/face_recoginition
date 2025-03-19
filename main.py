from fastapi import FastAPI
import os
import sys
from fastapi.middleware.cors import CORSMiddleware
from middlewares.middleware import catch_exceptions_middleware
from api.controller import router
sys.dont_write_bytecode = True

import logging
logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

app = FastAPI(
    title = 'FACE DETECTION',
    description = "This API was built with FastAPI.",
    version = "1.0.0",
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware('http')(catch_exceptions_middleware)


app.include_router(router)