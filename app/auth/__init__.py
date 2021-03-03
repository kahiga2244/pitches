from flask import Blueprint
from flask_mail import Mail

mail = Mail()
def create_app(config_name):
    app = Flask(__name__)

    mail.init_app(app)

auth = Blueprint('auth', __name__)

from . import views,forms