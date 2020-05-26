from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap



app = Flask('fyb')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
app.config.from_pyfile('settings.py')


from fyb import controllers, forms, models, views