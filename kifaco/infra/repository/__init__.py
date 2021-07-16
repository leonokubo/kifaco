from kifaco.domain.entity import Entity
from kifaco.infra.config import Conn


class Repository:
    entity: Entity

    @property
    def db_set(self):
        return Conn().session.query(self.entity)
