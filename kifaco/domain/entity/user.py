from sqlalchemy import BIGINT
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, SMALLINT
from sqlalchemy.orm import object_session
from sqlalchemy.orm import relationship

from kifaco.domain.entity import Entity
from kifaco.domain.entity.diet import Diet
from kifaco.domain.entity.household_appliance import HouseholdAppliance
from kifaco.domain.entity.menu import Menu


class UserMenu(Entity):
    __tablename__ = "user_x_menu"
    id: int = Column(BIGINT, primary_key=True, autoincrement=True)
    user: str = Column(BIGINT)
    menu: int = Column(BIGINT, ForeignKey(Menu.id))
    relation_menu = relationship(Menu)


class UserHouseholdAppliance(Entity):
    __tablename__ = "user_x_household_appliance"
    id: int = Column(BIGINT, primary_key=True, autoincrement=True)
    user: int = Column(BIGINT)
    household_appliance: int = Column(SMALLINT, ForeignKey(HouseholdAppliance.id))
    relation_household_appliance = relationship(HouseholdAppliance)


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

    @property
    def household_appliance(self):
        return object_session(self) \
            .query(UserHouseholdAppliance) \
            .join(HouseholdAppliance) \
            .with_entities(HouseholdAppliance) \
            .filter(UserHouseholdAppliance.user == self.id) \
            .all()

    @property
    def password(self):
        raise PermissionError("PermissionError")

    def to_json(self):
        return {
            "name": self.name,
            "diet": self.relation_diet.kind,
        }
