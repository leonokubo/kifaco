from sqlalchemy import Column, Integer, VARCHAR, TIME, JSON, ForeignKey, Enum, BIGINT
from sqlalchemy.orm import object_session
from sqlalchemy.orm import relationship

from kifaco.domain.Enum import Measurement
from kifaco.domain.entity import Entity
from kifaco.domain.entity.diet import Diet
from kifaco.domain.entity.ingredients import Ingredients
from kifaco.domain.entity.types_meal import TypesMeal


class MenuIngredients(Entity):
    __tablename__ = "menu_x_ingredients"
    id: int = Column(BIGINT, primary_key=True, autoincrement=True)
    amount: int = Column(Integer)
    unit_of_measurement: Measurement = Column(Enum(Measurement))
    menu: int = Column(Integer)

    ingredients: int = Column(Integer, ForeignKey(Ingredients.id))
    relation_ingredients = relationship(Ingredients)


class Menu(Entity):
    __tablename__ = "menu"
    id: int = Column(BIGINT, primary_key=True, autoincrement=True)
    plate: str = Column(VARCHAR(150))
    calorie: int = Column(Integer)
    time: str = Column(TIME)
    complement: str = Column(JSON)

    diet: int = Column(Integer, ForeignKey(Diet.id))
    relation_diet = relationship(Diet)

    types_meal: int = Column(Integer, ForeignKey(TypesMeal.id))
    relation_types_meal = relationship(TypesMeal)

    @property
    def ingredients(self):
        return object_session(self) \
            .query(MenuIngredients) \
            .join(Ingredients) \
            .with_entities(Ingredients.ingredients, Ingredients.kind) \
            .filter(MenuIngredients.menu == self.id) \
            .all()
