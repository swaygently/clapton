from oslo_log import log

from datetime import datetime
import flask
from flask import request
from flask_restful import Resource, fields, reqparse, marshal_with, abort


LOG = log.getLogger(__name__)


class OrderList(Resource):
    def get(self):
        '''
        response = flask.make_response('[{"id": 123}]', 200)
        response.headers.extend({'X-Pagination-Total-Count': 1000,
                                 'Content-Type': 'application/json; charset=utf-8'})
        return response
        '''
        return [{"id": 123}], 200, {'X-Pagination-Total-Count': 1000}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'total_amount',
            dest='total_amount',
            type=str,
            location='form',  # form, args, headers, cookies, json, files
            required=True,
            help='The orders\'s total amount',
        )
        args = parser.parse_args()
        LOG.debug(args)
        LOG.debug(args.total_amount)
        return {}, 201


class Order(Resource):
    @marshal_with({'id': fields.String, 'created_at': fields.DateTime, 'links': fields.Nested({'items': fields.Url('items', absolute=True)})})
    def get(self, order_id):
        return {'id': 123, 'created_at': datetime.now(), 'links':[]}

    def put(self, order_id):
        LOG.debug(request.form)
        LOG.debug(request.json)
        LOG.debug(dir(request))
        return {}, 201

    def delete(self, order_id):
        abort(500)
        # raise ValueError('haha')
        # raise werkzeug.exceptions.HTTPException(500)
        # raise werkzeug.exceptions.InternalServerError
        return '', 204


class OrderItemList(Resource):
    def get(self, order_id):
        return []
