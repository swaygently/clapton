from oslo_config import cfg

from oslo_db.sqlalchemy import enginefacade
from oslo_db.sqlalchemy.session import EngineFacade, create_engine, get_maker, Query, Session

from clapton.db.sqlalchemy import models


def get_backend():
    return SqlalchemyBackend()


@enginefacade.transaction_context_provider
class Conext(object):
    pass


class SqlalchemyBackend(object):

    @enginefacade.reader
    def list_orders(self, context):
        return context.session.query(models.Order).all()

    @enginefacade.reader
    def list_order_details(self, context):
        return context.session.query(models.OrderDetail).all()

    @enginefacade.writer
    def create_order(self, context):
        context.session.add(models.Order())

