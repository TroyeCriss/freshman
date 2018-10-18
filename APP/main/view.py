#coding:utf-8
#对主要的请求，进行反馈
from flask import render_template
from .import main 

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/tips')
def tips():
    return render_template('tips.html')

@main.route('/community/best')
def best():
    return render_template('best.html')

@main.route('/community/xk')
def xk():
    return render_template('xk.html')

@main.route('/community/ly')
def ly():
    return render_template('ly.html')

@main.route('/community/xf')
def xf():
    return render_template('xf.html')

@main.route('/community/gs')
def gs():
    return render_template('gs.html')

@main.route('/community/tj')
def tj():
    return render_template('tj.html')

@main.route('/community/wy')
def wy():
    return render_template('wy.html')
