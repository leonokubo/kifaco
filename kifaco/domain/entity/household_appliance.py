from sqlalchemy import Column, VARCHAR, SMALLINT

from kifaco.domain.entity import Entity


class HouseholdAppliance(Entity):
    __tablename__ = "household_appliance"
    id: int = Column(SMALLINT, primary_key=True, autoincrement=True)
    name: str = Column(VARCHAR(100))

    def to_json(self):
        return self.name
