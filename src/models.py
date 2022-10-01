import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column (String(250), nullable=False)
    password = Column (String(250), nullable=False)
    posts = relationship("Post")
    stories = relationship("Story")
    comentarios = relationship("Comentario")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image = Column (String(250), nullable=False)
    texto = Column (String(250), nullable=True)
    locacion = Column (String(250), nullable=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_comentario = Column(Integer, ForeignKey('comentario.id'))
    

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    image = Column (String(250), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_comentario = Column(Integer, ForeignKey('comentario.id'))
    

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    texto = Column (String(250), nullable=False)
    id_post = Column(Integer, ForeignKey('post.id'))
    id_story = Column(Integer, ForeignKey('story.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    posts = relationship("Post")
    stories = relationship("Story")

"""class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    id_personaje = Column(Integer, ForeignKey('personaje.id'))
    id_planeta = Column(Integer, ForeignKey('planeta.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
"""

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