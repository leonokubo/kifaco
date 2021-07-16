from sqlalchemy import Column, Integer, BIGINT, ForeignKey
from sqlalchemy.orm import relationship

from kifaco.domain.entity import Entity
from kifaco.domain.entity.ingredients import Ingredients
from kifaco.domain.entity.user import User


class Blacklist(Entity):
    __tablename__ = "blacklist"
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    user: int = Column(BIGINT, ForeignKey(User.id))
    relation_user = relationship(User)

    ingredients: int = Column(BIGINT, ForeignKey(Ingredients.id))
    relation_ingredients = relationship(Ingredients)
