from fastapi import FastAPI
from .routers import addressRoute, customerRoute

app = FastAPI()
app.include_router(customerRoute.router)
app.include_router(addressRoute.router)
