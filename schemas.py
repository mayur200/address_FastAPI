import imp
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel



T = TypeVar('T')

class CreateAddressSchema(BaseModel):
    id: int
    latitude:str
    longitude:str
    address_from_cordinates: Optional[str]=None

    class Config:
        orm_mode = True



class AddressSm(CreateAddressSchema):
    id: int

    class Config:
        orm_mode = True


class PaginatedAddrInfo(BaseModel):
    limit: int
    offset: int
    data: List[AddressSm]

