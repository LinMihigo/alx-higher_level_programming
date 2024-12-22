#!/usr/bin/python3
"""
Class definition of State

Attributes:
    Base (sqlalchemy.ext.declarative.api.DeclarativeMeta): maps python classes
    to db tables
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    The State class inheriting from Base

    Args:
        Base (sqlalchemy.ext.declarative.api.DeclarativeMeta): maps python
        classes to db tables

    Attributes:
        id (int): id
        name (str): name string
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
