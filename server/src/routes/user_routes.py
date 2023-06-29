from repositories.user_repository import UserRepository
from use_cases.user_use_cases import UserUseCase

from flask import Blueprint, session, redirect, request



user_bp = Blueprint('user', __name__)


@user_bp.route("/user/update/<int:id>", methods=["POST"])
def user_update(id) :
    repository = UserRepository()
    use_case = UserUseCase(repository)

    user = session.get("user", None)
    if not user :
        session["flash"] = "Entre na sua conta para acessar seu perfil"
        return redirect("/entrar")

    data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "cpf": request.form.get("cpf"),
        "birth_date": request.form.get("birth_date"),
        "photo": request.files["photo"] if request.files["photo"] else None,
        "password": request.form.get("password"),
        "created_at": user["created_at"]
    }

    try :
        use_case.update(data, user)

        updated_user = UserRepository.query.filter_by(id=user["id"]).first()
        
        session["user"] = updated_user.as_dict()

        session["flash"] = "Dados editados com sucesso!"
        return redirect("/perfil")
    
    except Exception as e:
        session["flash"] = e.args[0]
        return redirect("/perfil/editar")


@user_bp.route("/user/delete/<int:id>", methods=["POST"])
def user_delete(id):
    repository = UserRepository()
    use_case = UserUseCase(repository)

    user = session.get("user", None)

    if not user :
        session["flash"] = "Entre na sua conta para acessar seu perfil"
        return redirect("/entrar")

    try :
        deleted_user = use_case.delete(user)

        if not deleted_user :
            session["flash"] = "Não foi possível deletar seu perfil"
            return redirect("/perfil/apagar")
        
        session["flash"] = "Dados deletados com sucesso!"
        session.pop("user", None)
        return redirect("/entrar")
    
    except Exception as e :
        session["flash"] = e.args[0]
        return redirect("/perfil/apagar")