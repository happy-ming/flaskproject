from flask import Flask
from flask_migrate import Migrate

from models import User,Address
from exts import db
import config

app = Flask(__name__)
# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask_sql_yingshe'
# 动态追踪修改设置，如未设置只会提示警告，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

#把app绑定到db上
db.init_app(app)

# 迁移，绑定app和数据库
migrate = Migrate(app,db)



@app.route('/')
def hello_world():
    user1 = User(username='张三')
    db.session.add(user1)
    db.session.commit()

    address1 = Address(email_address='22856393@qq.com',user_id=user1.id)
    db.session.add(address1)
    db.session.commit()

    return 'Hello World!'


if __name__ == '__main__':
    db.create_all()
    app.run()

'''
使用命令进行映射
    1、初始化迁移文件夹   flask db init
    2、将当前模型添加到迁移文件夹 flask db migrate
    3、再把迁移文件夹对应的数据库操作，真正的映射到数据库中  flask db upgrade
'''
