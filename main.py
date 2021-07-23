from flask import Flask, Response

from kifaco.infra.router import FactoryRouter

app = Flask(__name__)
app.register_blueprint(FactoryRouter().blueprint)


@app.after_request
def handle_after_request(response: Response):
    return response


@app.errorhandler(Exception)
def handle_app_general_exception(error: Exception):
    return str(error)
