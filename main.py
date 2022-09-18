from typing import Union
from fastapi_utils.cbv import cbv
from fastapi import FastAPI
from . import crud, models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship,Session
from fastapi import APIRouter, Depends, HTTPException
from .schemas import CreateAddressSchema,PaginatedAddrInfo
from .crud import create_address,get_all_address,delete_address_info,update_address_info
from .exceptions import AddressNotFoundError,AddressException
from .models import Address
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="geoapiExercises")


app = FastAPI()

router = APIRouter()

models.Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#Class based view
@cbv(router)
class AddressView:
    session: Session = Depends(get_db)

    # API to get the list of Address info
    @router.get("/address", response_model=PaginatedAddrInfo)
    def list_addr(self, limit: int = 10, offset: int = 0):


        address_list = get_all_address(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": address_list}

        return response

    # API endpoint to add a Address info to the database
    @router.post("/address")
    def add_address(self, addr_info: CreateAddressSchema):
        try:
        
            #Get the address from latitude and longitude
            latitude = ""
            longitude = ""
            for rec in addr_info:
                if rec[0] == "latitude":
                    latitude = rec[1]
                elif rec[0] == "longitude":
                    longitude = rec[1]
            location = geolocator.geocode(latitude + "," + longitude)
            # addr_info = list(addr_info)
            # addr_info[3]= (addr_info[3][0], str(location))
            # addr_info = tuple(addr_info)
            addr_info = create_address(self.session, addr_info)
            return addr_info
        except AddressException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to update a Address info to the database
@router.put("/address/{address_id}")
def update_address(address_id: int, new_info: CreateAddressSchema, session: Session = Depends(get_db)):
    print("update_address@@@@")
    try:
        address_info = update_address_info(session, address_id, new_info)
        print("address_info@@@@",address_info)
        return address_info
    except AddressException as cie:
        raise HTTPException(**cie.__dict__)

# API endpoint to delete a Address info to the database
@router.delete("/address/{addr_id}")
def delete_addr(addr_id: int, session: Session = Depends(get_db)):
    try:
        return delete_address_info(session, addr_id)
    except AddressException as cie:
        raise HTTPException(**cie.__dict__)



app.include_router(router)
