from oslo_config import cfg

from flask import Flask, current_app, g
from flask_restful import Api

from clapton.api.resources import order

app = Flask(__name__)
#app.config['DEBUG'] = cfg.CONF.debug
with app.app_context():
    print dir(app)
    api = Api(app, catch_all_404s=True)
    print current_app

    '''
    curl /v1/orders
    curl -X POST -d '{}' -H 'Content-Type:application/json' /v1/orders
    curl /v1/orders/<order_id>
    curl -X PUT -d '{}' -H 'Content-Type:application/json' /v1/orders/<order_id>
    curl /v1/orders/<order_id>/items
    '''
    api.add_resource(order.OrderList, '/v1/orders')
    api.add_resource(order.Order, '/v1/orders/<string:order_id>')
    api.add_resource(order.OrderItemList, '/v1/orders/<string:order_id>/items')

    """
    api.add_resource(warehouse, '/v1/warehouses')
    api.add_resource(warehouse, '/v1/warehouse_product_locations')
    api.add_resource(warehouse, '/v1/stocks')
    api.add_resource(warehouse, '/v1/stock_movements')
    api.add_resource(warehouse, '/v1/stock_availables')
    api.add_resource(warehouse, '/v1/stock_movement_reasons')
    """
