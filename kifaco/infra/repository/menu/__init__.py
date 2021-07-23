from kifaco.domain.entity.user import Menu
from kifaco.infra.repository import Repository


class MenuRepository(Repository):
    entity = Menu
