from fastapi import APIRouter, status

from src.models import model
from src.services import address_services


router = APIRouter()


@router.get('', status_code=status.HTTP_202_ACCEPTED)
def all_address():
    return address_services.get_all()


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_address(address: model.Address):
    return address_services.create_address(address)


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
# should update optional fields
def update_address(id: int, address: model.Address):
    return address_services.update_address(address)


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete_address(id: int):
    return address_services.update_address(id)


@router.get('/{id}', status_code=status.HTTP_202_ACCEPTED)
def get_address(id: int):
    return address_services.get_address(id)


@router.get('/customer/{id}', status_code=status.HTTP_200_OK)
def get_address_from_customer(id: int):
    address_id = address_services.get_address_id_from_customer(id)
    return address_services.get_address(address_id)
