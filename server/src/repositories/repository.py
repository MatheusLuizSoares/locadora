from app import db
from sqlalchemy.ext.declarative import declarative_base 


class Repository () :
    def insert (self) :
        db.session.add(self)
        db.session.commit()
        db.session.close()


    def update (self) :
        db.session.commit()
        db.session.close()


    def delete (self) :
        db.session.delete(self)
        db.session.commit()
        db.session.close()