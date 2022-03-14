from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import APIRouter, status,Depends
from src.models.model import BaseAddress, GetAddress
from src.db.db import get_db
from src.services.address_services import get_all, create_address, update_address, get_address, get_address_id_from_customer, delete_address


router = APIRouter()


@router.get('', status_code=status.HTTP_200_OK,response_model=List[GetAddress])
def all_address(db:Session=Depends(get_db)):
    return get_all(db)


@router.post('/create', status_code=status.HTTP_201_CREATED,response_model=GetAddress)
def create(address: BaseAddress,db:Session=Depends(get_db)):
    return create_address(address,db)


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED,response_model=GetAddress)
# should update optional fields
def update(id: UUID, address: BaseAddress,db:Session=Depends(get_db)):
    return update_address(id, address,db)


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete(id: UUID,db:Session=Depends(get_db)):
    return delete_address(id,db)


@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=GetAddress)
def get(id: UUID,db:Session=Depends(get_db)):
    return get_address(id,db)


@router.get('/customer/{id}', status_code=status.HTTP_200_OK,response_model=GetAddress)
def show_address_from_customer(id: UUID,db:Session=Depends(get_db)):
    address_id = get_address_id_from_customer(id,db)
    return get_address(address_id,db)
