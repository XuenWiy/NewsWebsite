from info import create_app,db,models
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate

app = create_app("develop")

# 创建ｍａｎａｇｅｒ对象，管理ａｐｐ
manager = Manager(app)

# 使用Ｍｉｇｒａｔｅ关联ａｐｐ，ｄｂ
Migrate(app,db)

# 给ｍａｎａｇｅｒ添加一条操作条件
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()
