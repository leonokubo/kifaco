from kifaco.domain.entity.user import User
from kifaco.infra.repository import Repository

r = Repository()
r.entity = User
x = r.db_set.all()
