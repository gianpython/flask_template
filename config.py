class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    IMAGE_UPLOADS = "C:\Python3\myscript\TMP"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    IMAGE_UPLOADS = "C:\Python3\myscript\TMP"
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    CLIENT_CSV = "C:\Python3\myscript\TMP\CSV"
    CLIENT_IMG = "C:\Python3\myscript\TMP"


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = False
