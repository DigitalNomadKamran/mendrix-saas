from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import accounts, insights, properties

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mendrix Rentals Optimization API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(properties.router)
app.include_router(accounts.router)
app.include_router(insights.router)


@app.get("/")
def root():
    return {"message": "Mendrix Rentals API is running"}
