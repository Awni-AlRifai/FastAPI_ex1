from fastapi import FastAPI
from .routers import address_route, customer_route

app = FastAPI()
app.include_router(customer_route.router)
app.include_router(address_route.router)
