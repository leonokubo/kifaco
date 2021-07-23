from kifaco.domain.core.handler import HandlerABC
from kifaco.infra.repository.menu import MenuRepository


class Menu(HandlerABC):
    repository = MenuRepository()
