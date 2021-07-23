from flask import Blueprint

from kifaco.handler.v1.menu import Menu
from kifaco.infra.router.router import Router


class MenuRouter(Router):

    @staticmethod
    def routes_blueprint(routes_blueprint: Blueprint):
        routes_blueprint.add_url_rule(
            "/v1/menu/<id>",
            view_func=Menu.as_view("menu"), methods=["GET"])
        routes_blueprint.add_url_rule(
            "/v1/menu/<id>/<p1>",
            view_func=Menu.as_view("menu_1"), methods=["GET"])
        routes_blueprint.add_url_rule(
            "/v1/menu/<id>/<p1>/<p2>",
            view_func=Menu.as_view("menu_2"), methods=["GET"])
        routes_blueprint.add_url_rule(
            "/v1/menu/<id>/<p1>/<p2>/<p3>",
            view_func=Menu.as_view("menu_3"), methods=["GET"])
