import os
base_dir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY="Yang jing kang"
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(base_dir,"data-dev.sqlite")

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(base_dir,"data-test.sqlite")

class ProdutionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "data.sqlite")

config={
"development":DevelopmentConfig,
"testing":TestingConfig,
"production":ProdutionConfig,
"default":DevelopmentConfig}
