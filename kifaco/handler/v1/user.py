from kifaco.domain.core.handler import HandlerABC
from kifaco.infra.repository.user import UserRepository


class User(HandlerABC):
    user_repository = UserRepository()

    def get(self, **kwargs):
        data = {"user": self.user_repository.get(kwargs.get("id"))}
        for _, v in enumerate(kwargs.values()):
            data.update({v: getattr(data["user"], v)}) if hasattr(data["user"], v) else ...

        return self.response(data, 202)
