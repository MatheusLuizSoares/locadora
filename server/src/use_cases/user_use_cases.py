from repositories.user_repository import UserRepository
from helpers.validate import validate_email, validate_cpf, validate_photo

from datetime import datetime

import bcrypt, time, os


class UserUseCase () :
    def __init__ (self, repository) :
        self.repository = repository


    def update (self, user_data, signed_user) :
        if not user_data["name"] :
            raise Exception("O nome do usuário não pode ser vazio...")

        if not user_data["email"] or not validate_email(user_data["email"]) :
            raise Exception("O email passado é inválido...")
        
        email_exists = self.repository.query.filter_by(email=user_data["email"]).first()
        
        if email_exists and email_exists.id != signed_user["id"] :
            raise Exception("Email já cadastrado no sistema...")
        
        valid_cpf = validate_cpf(user_data["cpf"])
        
        if not user_data["cpf"] or not valid_cpf :
            raise Exception("O CPF passado não é válido...")
        
        cpf_exists = self.repository.query.filter_by(cpf=valid_cpf).first()
        if cpf_exists.id != signed_user["id"] :
            raise Exception("CPF já cadastrado no sistema...")

        if not user_data["password"] :
            raise Exception("A senha do usuário não pode ser vazia...")
        
        if not user_data["birth_date"] :
            raise Exception("A data de nascimento do usuário não pode ser vazia...")
        
        if user_data["photo"] :
            valid_extension = validate_photo(user_data["photo"])
            if not validate_photo(valid_extension) :
                raise Exception("O formato da foto é inválido...")
            
            os.remove(user_data["photo"])
            new_filename = f"{time.time()}.{valid_extension}"
            user_data["photo"].save(f"static/{new_filename}")
            

        user = self.repository.query.filter_by(id=signed_user["id"]).first()
        
        password_checked = bcrypt.checkpw(user_data["password"].encode("utf-8"), user.password.encode("utf-8"))
        
        if not password_checked :
            raise Exception("A senha do usuário está incorreta...")


        user.name = user_data["name"]
        user.email = user_data["email"]
        user.cpf = user_data["cpf"]
        user.birth_date = user_data["birth_date"]
        user.photo = new_filename if user_data["photo"] else signed_user["photo"]
        user.created_at = user_data["created_at"]
        user.updated_at = str(datetime.now())

        user.update()


    def delete (self, signed_user) :

        user = self.repository.query.filter_by(id=signed_user["id"]).first()

        if user.id != signed_user["id"] :
            raise Exception("Você não tem permissão para excluir este usuário...")

        user.delete()

        return True


    def signin (self, user_data) :
        if not user_data["name"] :
            raise Exception("O nome do usuário não pode ser vazio...")

        if not user_data["email"] or not validate_email(user_data["email"]) :
            raise Exception("O email passado é inválido...")
        
        email_exists = self.repository.query.filter_by(email=user_data["email"]).first()
        
        if email_exists :
            raise Exception("Usuário já cadastrado. Não gostaria de realizar login?")
        
        valid_cpf = validate_cpf(user_data["cpf"])
        
        if not user_data["cpf"] or not valid_cpf :
            raise Exception("O CPF passado não é válido...")
        
        cpf_exists = self.repository.query.filter_by(cpf=valid_cpf).first()

        if cpf_exists :
            raise Exception("CPF já cadastrado no sistema...")

        if not user_data["password"] :
            raise Exception("A senha do usuário não pode ser vazia...")
        
        if not user_data["birth_date"] :
            raise Exception("A data de nascimento do usuário não pode ser vazia...")
        
        
        user_age = datetime.now().year - datetime.strptime(user_data["birth_date"], "%Y-%m-%d").year

        print(user_age)

        if user_age > 120 :
            raise Exception("Sua idade é inválida para criar uma conta no sistema...")
        
        if user_age < 18 :
            raise Exception("Você precisa ser maior de idade para criar uma conta no sistema...")


        if user_data["photo"] :
            valid_extension = validate_photo(user_data["photo"].filename)
            if not valid_extension :
                raise Exception("O formato da foto é inválido...")
            
            new_filename = f"{time.time()}.{valid_extension}"
            user_data["photo"].save(f"static/{new_filename}")
        

        now = str(datetime.now())
        hashed_password = bcrypt.hashpw(user_data["password"].encode("utf-8"), bcrypt.gensalt())
        
        user = UserRepository(
            name=user_data["name"], 
            email=user_data["email"], 
            password=hashed_password, 
            cpf=valid_cpf,
            birth_date=user_data["birth_date"],
            photo= new_filename if user_data["photo"] else None,
            access="client",
            created_at = now,
            updated_at = now
        )
        
        user.insert()

        return True


    def login (self, user_data) :
        if not user_data["email"] :
            raise Exception("O email do usuário não pode ser vazio...")

        if not user_data["password"] :
            raise Exception("A senha do usuário não pode ser vazia...")
        
        data = self.repository.query.filter_by(email=user_data["email"]).first()

        if not data :
            raise Exception("Usuário não localizado...")

        password_checked = bcrypt.checkpw(user_data["password"].encode("utf-8"), data.password.encode("utf-8"))
        
        if not password_checked :
            raise Exception("Usuário não localizado...")
        
        del data.password
        
        return data