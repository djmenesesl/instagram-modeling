import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column (String(250), nullable=False)
    gender = Column (String(250), nullable=True)
    image = Column (String(250), nullable=False)
    favoritos = relationship("Favorito")

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column (String(250), nullable=False)
    image = Column (String(250), nullable=False)
    favoritos = relationship("Favorito")

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    mail = Column (String(250), nullable=False)
    password = Column (String(250), nullable=False)
    favoritos = relationship("Favorito")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    id_personaje = Column(Integer, ForeignKey('personaje.id'))
    id_planeta = Column(Integer, ForeignKey('planeta.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    

"""class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
"""
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')