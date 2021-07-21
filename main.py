from flask import Flask, Response

from kifaco.infra.router import routes_blueprint

app = Flask(__name__)
app.register_blueprint(routes_blueprint)


@app.after_request
def handle_after_request(response: Response):
    return response


@app.errorhandler(Exception)
def handle_app_general_exception(error: Exception):
    ...
