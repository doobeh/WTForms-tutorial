import os

from flask import Flask

def hello():
    return 'hi'

def other():
    return 'foo'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    print(f"instance path: {app.instance_path}")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #database
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import frontend
    app.register_blueprint(frontend.bp)

    from . import blog
    app.register_blueprint(blog.bp)

    return app


# a simple page that says hello
# @app.route('/hello')
# def hello():
#     return 'Hello, World!'