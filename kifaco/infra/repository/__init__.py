from kifaco.domain.entity import Entity
from kifaco.infra.config import Conn
from kifaco.infra.singleton import Singleton


class Repository(metaclass=Singleton):
    entity: Entity
    __session = False

    def __init__(self):
        self.__session = Conn().session

    @property
    def db_set(self):
        return self.__session.query(self.entity)

    def get(self, _id):
        return self.db_set.get(_id)

    def save(self, data):
        self.__session.add(data)

    def commit(self):
        self.__session.commit()
