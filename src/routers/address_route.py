from uuid import UUID
from fastapi import APIRouter, status

from src.models.model import Address
from src.services.address_services import get_all, create_address, update_address, get_address, get_address_id_from_customer, delete_address


router = APIRouter()


@router.get('', status_code=status.HTTP_200_OK)
def all_address():
    return get_all()


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create(address: Address):
    return create_address(address)


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
# should update optional fields
def update(id: UUID, address: Address):
    return update_address(id, address)


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete(id: UUID):
    return delete_address(id)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get(id: UUID):
    return get_address(id)


@router.get('/customer/{id}', status_code=status.HTTP_200_OK)
def show_address_from_customer(id: UUID):
    address_id = get_address_id_from_customer(id)
    return get_address(address_id)
