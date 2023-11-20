#!/usr/bin/python3
"""a python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
