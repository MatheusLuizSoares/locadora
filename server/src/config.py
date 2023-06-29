class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/a3-database-2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "PROJETO_A3_GRUPO_LOCADORA"
    UPLOAD_FOLDER = "/server/src/static"
    STATIC_FOLDER = "/server/src/static"