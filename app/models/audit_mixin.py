from datetime import datetime as dt
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declared_attr


class AuditMixin(object):
    """
    @declared_attr
    def created_by_id(cls):
        return Column(Integer, ForeignKey('users.id', name='fk_%s_created_by_id' % cls.__name__, use_alter=True), nullable=True)
    """

    created_at = Column(DateTime, nullable=False, default=dt.now())
    updated_at = Column(DateTime, nullable=False, default=dt.now(), onupdate=dt.now())
   