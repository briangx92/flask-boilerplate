from flask import Flask, request


def create_app(test_config=None): #Factory app
    app = Flask(__name__, instance_relative_config=True) #instantiating object

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index(): 
        print("-" * 20)
        print(f"Base URL: {request.base_url}")
        print("-" * 20)
        return 'This is a flask-boilerplate project, not to be used in production.'

    @app.route('/hello')
    def hello(name="World"):

        for key, value in request.args.items():
            print(f"{key}: {value}")

        name = request.args.get('name', 'World') # get the request from flask
        return f"Hello {name}!"
    
    @app.route('/number/<int:n>')
    def number_route(n):
        return f"number: {n}"
    

    return app