from sqlalchemy import Column, Integer, VARCHAR, Enum

from kifaco.domain.Enum import KindIngredients
from kifaco.domain.entity import Entity


class Ingredients(Entity):
    __tablename__ = "ingredients"
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    ingredients: str = Column(VARCHAR(100))
    kind: KindIngredients = Column(Enum(KindIngredients), nullable=False)
