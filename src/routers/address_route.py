from fastapi import APIRouter, status, HTTPException

from ..models import model
from ..db import db
from ..services import address_services


router = APIRouter()


@router.get('/api/v1/adress', status_code=status.HTTP_202_ACCEPTED)
def all_adresss():
    return address_services.get_all()


@router.get('/api/v1/adress/{id}', status_code=status.HTTP_202_ACCEPTED)
def get_address(id: int):
    return address_services.get_address(id)


@router.post('/api/v1/adress', status_code=status.HTTP_201_CREATED)
def create_adress(address: model.Adress):
    return address_services.create_address(address)


@router.put('/api/v1/adress/{id}', status_code=status.HTTP_202_ACCEPTED)
# should update optional fields
def update_adress(id: int, address: model.Adress):
    return address_services.update_address(address)


@router.delete('/api/v1/adress/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete_adress(id: int):
    return address_services.update_address(id)
