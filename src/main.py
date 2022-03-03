from fastapi import FastAPI
from .routers import customers, adresses

app = FastAPI()
app.include_router(customers.router)
app.include_router(adresses.router)
