from sqlalchemy import BIGINT
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from sqlalchemy.orm import object_session
from sqlalchemy.orm import relationship

from kifaco.domain.entity import Entity
from kifaco.domain.entity.diet import Diet
from kifaco.domain.entity.menu import Menu


class UserMenu(Entity):
    __tablename__ = "user_x_menu"
    id: int = Column(BIGINT, primary_key=True, autoincrement=True)
    user: str = Column(BIGINT)
    menu: int = Column(BIGINT, ForeignKey(Menu.id))
    relation_menu = relationship(Menu)


class User(Entity):
    __tablename__ = "user"
    id: int = Column(BIGINT, primary_key=True, autoincrement=True)
    name: str = Column(VARCHAR(250))
    password: str = Column(VARCHAR(100))

    diet: int = Column(Integer, ForeignKey(Diet.id))
    relation_diet = relationship(Diet)

    @property
    def menu(self):
        return object_session(self) \
            .query(UserMenu) \
            .join(Menu) \
            .with_entities(Menu) \
            .filter(UserMenu.user == self.id) \
            .all()
