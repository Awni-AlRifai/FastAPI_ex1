from fastapi import FastAPI
from src.routers import address_route, customer_route

app = FastAPI()
# Base.metadata.create_all(engine)


app.include_router(customer_route.router,
                   prefix="/customer", tags=['customers'])
app.include_router(address_route.router, prefix='/address', tags=['addresses'])
