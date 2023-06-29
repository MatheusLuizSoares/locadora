from repositories.repository import Repository
from app import db
from sqlalchemy import Column, Integer, String, Date, ForeignKey


class RentRepository (db.Model, Repository) :
    __tablename__ = 'rents'
    id = Column(Integer, primary_key=True)
    user_id = Column(None, ForeignKey("users.id"))
    movie_id = Column(None, ForeignKey("movies.id"))
    created_at = Column(Date)
    updated_at = Column(Date)


    def as_dict(self):
        return {

        }
