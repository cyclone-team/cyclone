# coding:utf-8
from flask import  Flask,request
from flask_cors import  *
from sqlalchemy.orm.exc import NoResultFound

from DBManager import *
from entities import  *
from utils import  *

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
