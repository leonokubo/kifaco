from sqlalchemy.ext.declarative import declarative_base


class Entity(declarative_base()):
    __abstract__ = True
    __hide_attr__ = ()
    __show_ppt__ = ()
