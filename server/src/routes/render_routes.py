from repositories.movie_repository import MovieRepository
from repositories.rent_repository import RentRepository

from use_cases.user_use_cases import UserUseCase
from use_cases.movie_use_cases import MovieUseCase

from flask import Blueprint, session, render_template, redirect
from datetime import datetime



render_bp = Blueprint("render", __name__)


# GET

@render_bp.route('/')
def index():
    user = session.get("user", None)
    site = {"title": "Página inicial"}
    
    repository = MovieRepository()
    use_case = MovieUseCase(repository)

    movies = use_case.get_all()
    
    flash = session.get('flash', None)
    session.pop("flash", None)

    return render_template('inicio.html', user=user, flash=flash, site=site, movies=movies)


@render_bp.route("/entrar")
def entrar():
    flash = session.get('flash', None)
    session.pop("flash", None)

    site = {"title": "Faça login"}
    user = session.get("user", None)

    if user :
        session["flash"] = "Você já está logado no sistema!"
        return redirect("/")

    return render_template("entrar.html", flash=flash, site=site, user=user)


@render_bp.route("/perfil")
def perfil():
    user = session.get("user", None)
    site = {"title": "Seu perfil"}
    flash = session.get("flash", None)
    session.pop("flash", None)
    rented_movies = []

    total_rent = 0
    user_rents = RentRepository.query.filter_by(user_id=user["id"]).all()
    for rent in user_rents :
        movie = MovieRepository.query.filter_by(id=rent.movie_id).first()
        rented_movies.append(movie)
        total_rent += movie.rent_price

    for rent in RentRepository.query.filter_by(user_id=id).all() :
        total_rent += MovieRepository.query.filter_by(id=rent.movie_id).rent_price

    if not user :
        session["flash"] = "Entre no sistema para acessar seu perfil"
        return redirect("/entrar")

    user_birth_timestamp = datetime.fromtimestamp(user["birth_date"].timestamp())

    time = datetime.now() - user_birth_timestamp
    user["age"] = time.days // 365

    return render_template("perfil.html", user=user, site=site, flash=flash, total_rent=total_rent, rented_movies=rented_movies)


@render_bp.route("/perfil/editar")
def perfil_editar():
    user = session.get("user", None)
    site = {"title": "Edite seu perfil"}
    flash = session.get("flash", None)
    session.pop("flash", None)

    if not user:
        session["flash"] = "Entre na sua conta para acessar seu perfil"
        return redirect("/entrar")
    
    return render_template("perfil_editar.html", user=user, site=site, flash=flash)


@render_bp.route("/perfil/apagar")
def perfil_apagar():
    user = session.get("user", None)
    site = {"title": "Apague sua conta"}
    flash = session.get("flash", None)
    session.pop("flash", None)

    if not user:
        session["flash"] = "Entre na sua conta para acessar seu perfil"
        return redirect("/entrar")
    
    return render_template("perfil_apagar.html", user=user, site=site, flash=flash)


@render_bp.route("/registrar")
def entrar_post():
    user = session.get("user", None)

    site = {"title": "Cadastre-se"}

    if user :
        session["flash"] = "Você já está logado no sistema!"
        return redirect("/")
    
    flash = session.get('flash', None)
    session.pop("flash", None)

    return render_template("registrar.html", flash=flash, site=site, user=user)


@render_bp.route("/filme/novo")
def filme_novo():
    user = session.get("user", None)
    site = { "title": "Admin: Cadastre um novo filme" }
    form_action = "/movie/create"

    flash = session.get('flash', None)
    session.pop("flash", None)

    if not user or user["access"] != "admin" :
        session["flash"] = "Cuidado: Você não tem acesso a essa página"
        return redirect("/")

    return render_template("filme_form.html", site=site, user=user, flash=flash, form_action=form_action)


@render_bp.route("/filme/<int:id>")
# /filme/9

def filme_inicio (id) :
    user = session.get("user", None)
    movie = MovieRepository.query.filter_by(id=id).first()

    if not movie :
        session["flash"] = "Filme não encontrado"
        return redirect("/")

    site = { "title": f"Inicio {movie.title}" }

    flash = session.get('flash', None)
    session.pop("flash", None)

    return render_template("filme_inicio.html", site=site, user=user, movie=movie, flash=flash)


@render_bp.route("/filme/editar/<int:id>")
def filme_editar (id) :
    user = session.get("user", None)
    movie = MovieRepository.query.filter_by(id=id).first()
    site = { "title": f"Editar {movie.title}" }
    form_action = f"/movie/update/{id}"

    if user["access"] != "admin" :
        session["flash"] = "Cuidado: Você não tem acesso a essa página"
        return redirect("/")
    
    if not movie :
        session["flash"] = "Filme não encontrado"
        return redirect("/")

    flash = session.get('flash', None)
    session.pop("flash", None)

    return render_template("filme_form.html", site=site, user=user, movie=movie, flash=flash, form_action=form_action)


@render_bp.route("/filme/apagar/<int:id>")
def filme_apagar (id) :
    user = session.get("user", None)
    movie = MovieRepository.query.filter_by(id=id).first()
    site = { "title": f"Apagar {movie.title}" }

    if user["access"] != "admin" :
        session["flash"] = "Cuidado: Você não tem acesso a essa página"
        return redirect("/")
    
    if not movie :
        session["flash"] = "Filme não encontrado"
        return redirect("/")

    return render_template("filme_apagar.html", site=site, user=user, movie=movie)


@render_bp.route("/alugar/<int:id>")
def alugar (id) :
    user = session.get('user', None)
    movie = MovieRepository.query.filter_by(id=id).first()
    site = { "title": "Alugue seu filme predileto!" }
    flash = session.get("flash", None)


    if not user :
        session["user"] = "Entre no seu perfil para acessar nosso sistema"
        return redirect("/entrar")
    
    if not movie :
        session["user"] = "Filme não encontrado"
        return redirect("/")
    
    return render_template("alugar.html", site=site, user=user, movie=movie, flash=flash)

    


     
    