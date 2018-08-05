#coding:utf-8
#flask实例属性配置
import os
basedir = os.path.abspath(os.path.dirname(__file__))
#flask实例基础属性配置
class Config:
    SECRET_KEY='Hard to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    FLASKY_MAIL_SUBJECT_PREFIX='[Flasky]'
    FLASKY_MAIL_SENDER='10457192@qq.com'
    FLASKY_ADMIN='10457192@qq.com'
    
    @staticmethod
    def init_app(app):
        pass
#不同版本，所需要的特殊配置
class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass

#配置字典，键对应所需要的类
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}