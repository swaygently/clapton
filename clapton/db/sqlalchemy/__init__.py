from oslo_config import cfg

from oslo_db.sqlalchemy import enginefacade
from oslo_db.sqlalchemy.session import EngineFacade, create_engine, get_maker, Query, Session

from clapton.db.sqlalchemy import models


def get_backend():
    return SqlalchemyBackend.from_config(cfg.CONF)


class SqlalchemyBackend(object):

    def list_orders(self, context):
        with enginefacade.reader.using(context) as session:
            return session.query(models.Order).all()

    def list_order_details(self):
        return self.get_session().query(models.Order).all()

    def create_order(self, context):
        with enginefacade.writer.using(context) as session:
            session.add(models.Order())

