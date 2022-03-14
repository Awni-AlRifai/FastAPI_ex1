from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import APIRouter, status,Depends
from src.models.model import BaseCustomer,GetCustomer
from src.db.db import get_db
from src.services.customer_services import create_customer, get_all, update_customer, delete_customer, get_customer


router = APIRouter()


@router.get('', status_code=status.HTTP_200_OK,response_model=List[GetCustomer])
def all_customers(db:Session=Depends(get_db)):
    return get_all(db)


@router.post('/create', status_code=status.HTTP_201_CREATED,response_model=GetCustomer)
def create(customer: BaseCustomer,db:Session=Depends(get_db)):
    return create_customer(customer,db)


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED,response_model=GetCustomer)
# should update optional fields
def update(id: UUID, customer: BaseCustomer,db:Session=Depends(get_db)):
    return update_customer(id, customer,db)


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete(id: UUID,db:Session=Depends(get_db)):
    return delete_customer(id,db)


@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=GetCustomer)
def show_customer(id: UUID,db:Session=Depends(get_db)):
    return get_customer(id,db)
    