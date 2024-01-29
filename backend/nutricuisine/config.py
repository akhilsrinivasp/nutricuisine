from dotenv import load_dotenv
import os
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
COMMON_DB=os.getenv('COMMON_DB') 
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')


class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    # SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"

class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = COMMON_DB
    DEBUG = True
    SECRET_KEY = SECRET_KEY
    UPLOAD_FOLDER=UPLOAD_FOLDER
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = COMMON_DB
    DEBUG = False
    SECRET_KEY = SECRET_KEY
    UPLOAD_FOLDER=UPLOAD_FOLDER
