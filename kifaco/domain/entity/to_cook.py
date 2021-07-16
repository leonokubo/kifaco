from sqlalchemy import Column, Integer, BIGINT, ForeignKey, TEXT
from sqlalchemy.orm import relationship

from kifaco.domain.entity import Entity
from kifaco.domain.entity.menu import Menu


class ToCook(Entity):
    __tablename__ = "to_cook"
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    cook: str = Column(TEXT)
    menu: int = Column(BIGINT, ForeignKey(Menu.id))
    relation_user = relationship(Menu)
