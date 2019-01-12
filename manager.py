


from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

class Config(object):
    # 调试信息
    DEBUG = True

    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/secondnews"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



app.config.from_object(Config)

#创建ＳＱＬＡｌｃｈｅｍｙ对象，关联ａｐｐ
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
