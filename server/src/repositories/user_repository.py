from repositories.repository import Repository
from app import db
from sqlalchemy import Column, Integer, String, Date


# ORM - Object Relational Maping



class UserRepository (db.Model, Repository) :
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    cpf = Column(String(11), nullable=False)
    photo = Column(String(255), nullable=False)
    birth_date = Column(Date)
    access = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(Date)
    updated_at = Column(Date)


    def as_dict (self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "cpf": self.cpf,
            "photo": self.photo,
            "birth_date": self.birth_date,
            "access": self.access,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }