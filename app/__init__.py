from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import settings

app = Flask(__name__)
app.config.from_object(settings)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.database_url

db = SQLAlchemy(app)

from . import views
from . import models
