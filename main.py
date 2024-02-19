import threading
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.source_router import SourceRouter

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins (e.g., frontend URLs)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

source_router = SourceRouter()
app.include_router(source_router.router)
