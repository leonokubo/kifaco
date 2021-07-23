from abc import ABC, abstractmethod

from flask import Blueprint


class Router(ABC):
    blueprint = Blueprint("routes_blueprint", __name__)

    @staticmethod
    @abstractmethod
    def routes_blueprint(routes_blueprint: Blueprint):
        raise NotImplementedError()
