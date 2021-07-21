from kifaco.domain.core.handler import HandlerABC
from kifaco.infra.repository.user import UserRepository


class User(HandlerABC):
    repository = UserRepository()
