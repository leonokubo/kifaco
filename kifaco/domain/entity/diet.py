from sqlalchemy import Column, Integer, VARCHAR

from kifaco.domain.entity import Entity


class Diet(Entity):
    __tablename__ = "diet"
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    kind: str = Column(VARCHAR(100))
