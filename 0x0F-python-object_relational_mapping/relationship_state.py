#!/usr/bin/python3
"""
    Module that performs creates a State class based off of Base.
"""
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
        The State class which inherits from the Base class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
