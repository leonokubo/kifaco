from sqlalchemy import Column, Integer, VARCHAR

from kifaco.domain.entity import Entity


class TypesMeal(Entity):
    __tablename__ = "types_meal"
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    meal: str = Column(VARCHAR(100))
