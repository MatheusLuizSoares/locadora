from repositories.movie_repository import MovieRepository
from repositories.rent_repository import RentRepository
from helpers.validate import validate_photo

from datetime import datetime
import time, os

class MovieUseCase () :
    def __init__ (self, repository) :
        self.repository = repository

    def get_all (self) :
        return self.repository.query.all()
    
    def create (self, movie_data) :
        if not movie_data["title"] :
            raise Exception ("O título do filme não pode estar vazio...")
        
        if not movie_data["year"] :
            raise Exception ("O ano não pode ser vazio...")
        
        if int(movie_data["year"]) < 1888 or int(movie_data["year"]) >= datetime.now().year :
            raise Exception ("O ano passado é inválido...")
        
        if not movie_data["genre"] :
            raise Exception ("O gênero do filme não pode estar vazio...")
        
        if not movie_data["rent_price"] :
            raise Exception ("O preço de aluguel não pode estar vazio...")
        

        if not movie_data["rent_price"].isdigit() or int(movie_data["rent_price"]) < 0 :
            raise Exception ("O preço de aluguel deve ser um número positivo...")
        
        now = str(datetime.now())


        if movie_data["photo"] :
            valid_extension = validate_photo(movie_data["photo"].filename)
            if valid_extension :
                new_filename = f"{time.time()}.{valid_extension}"
                movie_data["photo"].save(f"static/{new_filename}")
        
        movie = MovieRepository(
            title = movie_data["title"],
            year = movie_data["year"],
            genre = movie_data["genre"],
            photo = new_filename if movie_data["photo"] else "holder.png",
            rent_price = movie_data["rent_price"],
            created_at = now,
            updated_at = now
        )

        movie.insert()

        return True


    def update (self, movie_data, actual_movie) :
        if not movie_data["title"] :
            raise Exception ("O título do filme não pode estar vazio...")
        
        if not movie_data["year"] :
            raise Exception ("O ano não pode ser vazio...")
        
        if int(movie_data["year"]) < 1888 or int(movie_data["year"]) > datetime.now().year :
            raise Exception ("O ano passado é inválido...")
        
        if not movie_data["genre"] :
            raise Exception ("O gênero do filme não pode estar vazio...")
        
        if not movie_data["rent_price"] :
            raise Exception ("O preço de aluguel não pode estar vazio...")
        
        if not movie_data["rent_price"].isdigit() or int(movie_data["rent_price"]) < 0 :
            raise Exception ("O preço de aluguel deve ser um número positivo...")
        

        if movie_data["photo"] :
            valid_extension = validate_photo(movie_data["photo"].filename)
            
            if valid_extension :
                new_filename = f"{time.time()}.{valid_extension}"
                movie_data["photo"].save(f"static/{new_filename}")

                if movie_data["photo"] != "holder.png" :
                    os.remove(f"static/{actual_movie.photo}")
        

        actual_movie.title = movie_data["title"]
        actual_movie.year = movie_data["year"]
        actual_movie.genre = movie_data["genre"]
        actual_movie.rent_price = movie_data["rent_price"]
        actual_movie.photo = new_filename if movie_data["photo"] else actual_movie.photo
        actual_movie.created_at = actual_movie.created_at
        actual_movie.updated_at = str(datetime.now())

        actual_movie.update()


    def delete (self, movie_id) :
        movie = self.repository.query.filter_by(id=movie_id).first()

        if not movie :
            raise Exception("O filme não existe...")

        rents = RentRepository.query.filter_by(movie_id=movie_id)

        for rent in rents :
            rent.delete()

        if movie.photo and movie.photo != "holder.png":
            os.remove(f"static/{movie.photo}")

        movie.delete()
        
        return True
