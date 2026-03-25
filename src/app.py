import click
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

@click.command('init-db')
def init_db_command():
    global db
    with current_app.app_context():
     db.create_all()
    """Clear the existing data and create new tables."""
    click.echo('Initialized the database.')



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
      SQLALCHEMY_DATABASE_URI="sqlite:///dio_bank.sqlite",
    )

    if test_config is None:
        # load config from instance folder
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # simple route
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.cli.add_command(init_db_command)

    # initialize database
    db.init_app(app)

    return app