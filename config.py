"""FlaskのConfigを提供する"""
import os

from dotenv import load_dotenv

load_dotenv()

# Flask
DEBUG = True


class DevelopmentConfig:

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8".format(
        **{
            "user": os.getenv("DB_USER", os.environ["DB_USERNAME"]),
            "password": os.getenv("DB_PASSWORD", os.environ["DB_PASSWORD"]),
            "host": os.getenv("DB_HOST", os.environ["DB_HOSTNAME"]),
            "db_name": os.getenv("DB_DATABASE", os.environ["DB_NAME"]),
        }
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
