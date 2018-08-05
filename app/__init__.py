#coding:utf-8
#创建flask实例，并创建flask扩展包对象
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap

#创建flask扩展包对象
bootstrap=Bootstrap() 

#创建flask实例，并创建扩展包的对象
def create_app(config_name): 
    app = Flask(__name__) 
    #由config字典，获取所需flask实例的属性
    app.config.from_object(config[config_name])    
    config[config_name].init_app(app)
    #实例化flask扩展包对象 
    bootstrap.init_app(app)
    #注册蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app