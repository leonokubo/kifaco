from kifaco.infra.router.customer import CustomerRouter
from kifaco.infra.router.menu import MenuRouter
from kifaco.infra.router.router import Router

__all__ = [CustomerRouter, MenuRouter]


class FactoryRouter(object):
    routes_blueprint = Router

    def __init__(self):
        for klass in Router.__subclasses__():
            klass.routes_blueprint(self.routes_blueprint.blueprint)

    @property
    def blueprint(self):
        return self.routes_blueprint.blueprint
