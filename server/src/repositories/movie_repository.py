from repositories.repository import Repository
from app import db
from sqlalchemy import Column, Integer, String, Date


class MovieRepository (db.Model, Repository) :
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    year = Column(String(4), nullable=False)
    genre = Column(String(255), nullable=False)
    photo = Column(String(255), nullable=True)
    rent_price = Column(Integer, nullable=False)
    created_at = Column(Date)
    updated_at = Column(Date)


    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "photo": self.photo,
            "rent_price": self.rent_price,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
