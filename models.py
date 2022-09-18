from sqlalchemy import  Column, Integer, String, null
from .database import Base



class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(String, index=True)
    longitude = Column(String, index=True)
    address_from_cordinates = Column(String, index=True)


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")

