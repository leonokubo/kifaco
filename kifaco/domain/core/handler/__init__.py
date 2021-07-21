from typing import Union

from flask.views import MethodView

from kifaco.domain.entity import Entity
from kifaco.infra.repository import Repository


class HandlerABC(MethodView):
    repository: Repository

    @staticmethod
    def __prepare(value):
        response = value
        if isinstance(value, Entity):
            response = value.to_json()
        if isinstance(value, list):
            response = []
            for v in value:
                if isinstance(v, Entity):
                    response.append(v.to_json())

        return response

    def response(self, body: Union[dict, str], code: int = 200):
        response = {}
        if body is None:
            code = 404

        if not isinstance(body, str):
            for k, v in body.items():
                response.update({k: self.__prepare(v)})

        return {"data": response, "code": code}, code

    def get(self, **kwargs):
        key = self.__class__.__name__.lower()
        data = {key: self.repository.get(kwargs.get("id"))}
        for _, v in enumerate(kwargs.values()):
            data.update({v: getattr(data[key], v)}) if hasattr(data[key], v) else ...

        return self.response(data, 202)
