from fastapi import APIRouter, status, HTTPException
from ..schema import scheams, db


router = APIRouter()


@router.get('/api/v1/adress', status_code=status.HTTP_202_ACCEPTED)
def all_adresss():
    return db.fake_address_db


@router.get('/api/v1/adress/{id}', status_code=status.HTTP_202_ACCEPTED)
def get_adress(id: int):
    adressses = db.fake_address_db
    for adress in adressses:
        if adress['id'] == id:
            return adress
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to find was not found')


@router.post('/api/v1/adress', status_code=status.HTTP_201_CREATED)
def create_adress(adress: scheams.Adress):
    db.fake_address_db.append(adress)
    return 'created successfully'


@router.put('/api/v1/adress/{id}', status_code=status.HTTP_202_ACCEPTED)
# should update optional fields
def update_adress(id: int, adress: scheams.Adress):
    adresss = db.fake_address_db
    for saved_adress in adresss:
        if saved_adress['id'] == id:
            saved_adress = adress
            return 'updated successfully'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to update was not found')


@router.delete('/api/v1/adress/{id}', status_code=status.HTTP_204_NO_CONTENT)
# should update optional fields
def delete_adress(id: int):
    adresss = db.fake_address_db
    for saved_adress in adresss:

        if saved_adress['id'] == id:
            adresss.remove(saved_adress)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'The adress you are trying to update was not found')
