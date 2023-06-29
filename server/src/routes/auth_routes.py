from repositories.user_repository import UserRepository
from use_cases.user_use_cases import UserUseCase

from flask import Blueprint, request, session, redirect


auth_bp = Blueprint("auth", __name__)


# GET

@auth_bp.route("/sair")
def sair() :
    session.pop("user", None)

    return redirect("/entrar")


# POST

@auth_bp.route("/login", methods=["POST"])
def login() :
    repository = UserRepository()
    use_case = UserUseCase(repository)

    data = {
        "email": request.form.get("email"),
        "password": request.form.get("password")
    }

    try :
        user = use_case.login(data)
        
        session["user"] = user.as_dict()

        return redirect("/")


    except Exception as e:
        session["flash"] = e.args[0]
        return redirect("/entrar")


@auth_bp.route("/signin", methods=["POST"])
def signin():
    repository = UserRepository()
    use_case = UserUseCase(repository)

    data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "cpf": request.form.get("cpf"),
        "password": request.form.get("password"),
        "photo": request.files["photo"] if request.files["photo"] else None,
        "birth_date": request.form.get("birth_date")
    }

    try :
        use_case.signin(data) 

        session["flash"] = "Tudo certo! Agora faça login"
        return redirect("/entrar")
    
    except Exception as e :
        print(e)
        session["flash"] = e.args[0]
        return redirect("/registrar")