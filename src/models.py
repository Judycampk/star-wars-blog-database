import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250),nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250),nullable=False)

class People_Details(Base):
    __tablename__ = 'people_details'
    id = Column(Integer, primary_key=True)
    height = Column(Integer,nullable=False)
    mass = Column(Integer,nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    created = Column(Integer, nullable=False)
    edited = Column(Integer, nullable=False)
    name = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'))
    People = relationship(People)

class Planets_Details(Base):
    __tablename__ = 'planets_details'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer,nullable=False)
    rotation_period = Column(Integer,nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    created = Column(Integer, nullable=False)
    edited = Column(Integer, nullable=False)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    Planets_id = Column(Integer, ForeignKey('planets.id'))
    Planets = relationship(Planets)

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    photo = Column(String,nullable=False) 

class Favourites (Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    people = Column(Integer, ForeignKey('people.id'))
    planets = Column(Integer, ForeignKey('planets.id'))
    Favourites_id = Column(Integer, ForeignKey('user.id'))
    Favourites = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')