import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'dioback.sqlite'),
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

    # initialize database
    from . import db
    db.init_app(app)

    return app