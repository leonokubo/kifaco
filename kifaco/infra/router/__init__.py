from flask import Blueprint

from kifaco.handler.v1.user import User

routes_blueprint = Blueprint("routes_blueprint", __name__)

"""Customer"""
routes_blueprint.add_url_rule(
    "/v1/customer/<id>",
    view_func=User.as_view("customer"), methods=["GET"])
routes_blueprint.add_url_rule(
    "/v1/customer/<id>/<p1>",
    view_func=User.as_view("customer_1"), methods=["GET"])
routes_blueprint.add_url_rule(
    "/v1/customer/<id>/<p1>/<p2>",
    view_func=User.as_view("customer_2"), methods=["GET"])
routes_blueprint.add_url_rule(
    "/v1/customer/<id>/<p1>/<p2>/<p3>",
    view_func=User.as_view("customer_3"), methods=["GET"])
