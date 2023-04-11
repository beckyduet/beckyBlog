import os
from flask_migrate import Migrate
from .app import create_app, db
from .app.models import Post,User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

#避免重复创建表，使用装饰器创建并注册一个shell上下文处理器
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,
               Post=Post)


