from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import settings

app = Flask(__name__)
app.config.from_object(settings)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.database_url

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views
from . import models
