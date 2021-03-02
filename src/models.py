import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique = True, nullable=False)
    password = Column(String(250), nullable=False)
    photo = Column(String,nullable=False)

    favourite_planets = relationship("Fav_Planet", backref="user")
    favourite_people = relationship("Fav_People", backref="user")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "photo": self.photo
        }

class Fav_People (Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'),nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "people": self.people_id,
        }

class Fav_Planet (Base):
    __tablename__ = 'fav_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    planet_id= Column(Integer, ForeignKey('planet.id'),nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "planet": self.planet_id,
        }

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250),nullable=False)
    url = Column(Integer,nullable=False)
    mass = Column(Integer,nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    created = Column(Integer, nullable=False)
    edited = Column(Integer, nullable=False)
    homeworld = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    Like_by_users = relationship("Fav_People", backref="people")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "created": self.created,
            "edited": self.edited,
            "name": self.name,
            "homeworld": self.homeworld,
            "description": self.description,
        }

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250),nullable=False)
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
    Like_by_users = relationship("Fav_Planet", backref="planet")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')