from kifaco.domain.entity.user import User
from kifaco.infra.repository import Repository


class UserRepository(Repository):
    entity = User
