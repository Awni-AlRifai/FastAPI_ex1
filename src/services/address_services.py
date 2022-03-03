from fastapi import HTTPException, status

from ..models import model
from ..db import db

# we should handle the results seperately


def get_all():
    return db.fake_address_db


def get_address(id: int):
    adressses = db.fake_address_db
    for adress in adressses:
        if adress['id'] == id:
            return adress
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to find was not found')


def create_address(adress: model.Adress):
    db.fake_address_db.append(adress)
    return "created successfully"


def update_address(address: model.Adress):
    address = db.fake_address_db
    for save_address in address:
        if saved_address['id'] == id:
            saved_address = address
            return 'updated successfully'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to update was not found')


def delete_address(id: int):
    # should update optional fields
    adresss = db.fake_address_db
    for saved_adress in adresss:
        if saved_adress['id'] == id:
            adresss.remove(saved_adress)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to update was not found')
