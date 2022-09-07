from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['DEBUG'] = True
app.config[
        'SQLALCHEMY_DATABASE_URI'
        ] = "mysql+pymysql://krypton612:12345@localhost:3306/note_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

Migrate(app, db)

from app.config import routes
from app.config.routes import routes_protected, routes_not_protected
from app.config import models

app.register_blueprint(routes_not_protected, url_prefix="/")
app.register_blueprint(routes_protected, url_prefix="/")
