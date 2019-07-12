# coding:utf-8
from flask import  Flask,request
from flask_cors import  *
from sqlalchemy.orm.exc import NoResultFound

from DBManager import *
from entities import  *
from utils import  *

app=Flask(__name__)
#解决跨域问题
CORS(app,supports_credentials=True)
#解决中文显示问题
app.config['JSON_AS_ASCII']=False

#连接数据库
db_manager=DBManager("mysql+mysqlconnector","47.107.86.216:3306","root","0C45313cea34","timecontrol")
if db_manager is not None:
    print("DB is OK!")

# 创建新用户
@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    p_account = request.values.get("account")
    p_password = request.values.get("password")
    print(p_account,p_password)

    db_session = db_manager.create_session()

    try:
        user_exist = db_session.query(User).filter(User.account == p_account).one()
    except NoResultFound:
        user_exist = None

    if user_exist is None:
        user = User(account=p_account,password=p_password)
        db_session.add(user)
        db_session.commit()
        user_new = db_session.query(User).filter(User.account == p_account).one()
        msg = Message("创建用户成功", 1)
        str_json = user_new.to_json(msg)
    else:
        msg = Message("用户已存在", 2)
        str_json = user_exist.to_json(msg)

    db_session.close()

    return str_json


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
