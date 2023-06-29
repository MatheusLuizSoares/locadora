from repositories.rent_repository import RentRepository

from datetime import datetime

class RentUseCases () :
    def __init__ (self, repository) :
        self.repository = repository

    def create (self, rent_data) :
        now = str(datetime.now())

        rent_exists = self.repository.query.filter_by(user_id=rent_data["user_id"]).first()

        if rent_exists and rent_exists.movie_id == rent_data["movie_id"] :
            raise Exception("Você já está alugando esse filme")
        
        rent = RentRepository(
            user_id=rent_data["user_id"],
            movie_id=rent_data["movie_id"],
            created_at=now,
            updated_at=now
        )

        rent.insert()

        return True