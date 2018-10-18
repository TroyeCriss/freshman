#coding:utf-8
#主路由蓝图初始化
from flask import Blueprint

main=Blueprint('main',__name__) 

from .import error,view