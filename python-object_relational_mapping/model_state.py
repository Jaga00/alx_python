#a python file that contains the class definition of a State and an instance Base = declarative_base()

#!/usr/bin/env python3
"""
Module: model_state

Contains the class definition of a State and an instance Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class representing the State table in the MySQL database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)