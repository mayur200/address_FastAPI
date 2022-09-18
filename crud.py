# crud.py
from typing import List
from sqlalchemy.orm import Session
from .exceptions import AddressException, AddressNotFoundError
from .models import Address
from .schemas import CreateAddressSchema, AddressSm


# Function to get list of car info
def get_all_address(session: Session, limit: int, offset: int) -> List[Address]:
    return session.query(Address).offset(offset).limit(limit).all()


# Function to  get info of a particular car
def get_address_info_by_id(session: Session, _id: int) -> Address:
    addr_info = session.query(Address).get(_id)

    if addr_info is None:
        raise AddressNotFoundError

    return addr_info


# Function to add a new car info to the database
def create_address(session: Session, addr_info: CreateAddressSchema) -> Address:
    print("create_address@@@@")
    # addr_details = session.query(Address).filter(Address.id == addr_info.id).first()

    # if addr_details is not None:
    #     raise AddressNotFoundError
    print("addr_info@@@@",addr_info)
    new_addr_info = Address(**addr_info.dict())
    session.add(new_addr_info)
    session.commit()
    session.refresh(new_addr_info)
    return new_addr_info


# Function to update details of the car
def update_address_info(session: Session, _id: int, info_update: CreateAddressSchema) -> Address:
    addr_info = get_address_info_by_id(session, _id)

    if addr_info is None:
        raise AddressNotFoundError
    print("update_address_info@@@@",addr_info)
    addr_info.id = info_update.id
    addr_info.latitude = info_update.latitude
    addr_info.longitude = info_update.longitude
    session.commit()
    session.refresh(addr_info)

    return addr_info


# Function to delete a car info from the db
def delete_address_info(session: Session, _id: int):
    addr_info = get_address_info_by_id(session, _id)

    if addr_info is None:
        raise AddressNotFoundError

    session.delete(addr_info)
    session.commit()

    return
