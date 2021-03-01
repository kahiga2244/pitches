from app import create_app,db
from app.models import User
from flask_script import Manager,Server


# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run(debug = True)