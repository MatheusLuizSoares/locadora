from use_cases.rent_use_cases import RentUseCases

from repositories.rent_repository import RentRepository
from repositories.movie_repository import MovieRepository

from flask import Blueprint, redirect, session

rent_bp = Blueprint("rent", __name__)


@rent_bp.route("/rent/<int:id>", methods=["POST"])
def rent(id) :
    repository = RentRepository()
    use_case = RentUseCases(repository)
    
    user = session.get("user", None)
    movie = MovieRepository.query.filter_by(id=id).first()

    movie_title = movie.title
    movie_id = movie.id

    if not user :
        session["flash"] = "Entre no sistema para acessar seu perfil."
        return redirect("/entrar")
    
    if not movie :
        session["flash"] = "Filme não encontrado."
        return redirect("/")
    
    rent_data = {
        "user_id": user["id"],
        "movie_id": movie_id,
    }
    
    try :
        use_case.create(rent_data)

        session["flash"] = f"{movie_title} adicionado a sua lista de alugados"
        return redirect("/perfil")

    except Exception as e :
        session["flash"] = e.args[0]
        return redirect(f"/alugar/{movie_id}")