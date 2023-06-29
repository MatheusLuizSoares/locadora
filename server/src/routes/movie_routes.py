from repositories.movie_repository import MovieRepository
from use_cases.movie_use_cases import MovieUseCase

from flask import Blueprint, request, session, redirect



movie_bp = Blueprint("movie", __name__)


@movie_bp.route("/movie/create", methods=["POST"])
def movie_create():
    repository = MovieRepository()
    use_case = MovieUseCase(repository)

    data = {
        "title": request.form.get("title"),
        "year": request.form.get("year"),
        "genre": request.form.get("genre"),
        "photo": request.files["photo"] if request.files["photo"] else None,
        "rent_price": request.form.get("rent_price")
    }

    try :
        use_case.create(data)

        session["flash"] = "Filme criado com sucesso"
        return redirect("/")
    
    except Exception as e :
        session["flash"] = e.args[0]
        return redirect("/filme/novo")


@movie_bp.route("/movie/update/<int:id>", methods=["POST"])
def movie_update(id) :
    repository = MovieRepository()
    use_case = MovieUseCase(repository)

    movie = repository.query.filter_by(id=id).first()

    if not movie :
        session["flash"] = "Filme não encontrado"
        return redirect("/")

    data = {
        "title": request.form.get("title"),
        "year": request.form.get("year"),
        "genre": request.form.get("genre"),
        "photo": request.files["photo"] if request.files["photo"] else None,
        "rent_price": request.form.get("rent_price")
    }

    try :
        use_case.update(data, movie)

        session["flash"] = "Filme atualizado com sucesso"
        return redirect("/")
    
    except Exception as e :
        print(e)
        session["flash"] = e.args[0]
        return redirect(f"/filme/{id}")
    

@movie_bp.route("/movie/delete/<int:id>", methods=["POST"])
def movie_delete(id) :
    repository = MovieRepository()
    use_case = MovieUseCase(repository)
    user = session.get("user", None)
    
    if user["access"] != "admin" :
        session["flash"] = "Cuidado: Você não tem acesso a essa página"
        return redirect("/")
    
    try :
        if not use_case.delete(id) :
            raise Exception("Erro interno...")
        
        session["flash"] = "Filme deletado com sucesso!"
        return redirect("/")

    except Exception as e :
        session["flash"] = e.args[0]
        return redirect("/")
