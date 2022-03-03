from fastapi import FastAPI
from src.routers import address_route, customer_route

app = FastAPI()
app.include_router(customer_route.router, prefix="/customer")
app.include_router(address_route.router, prefix='/address')
