from oslo_log import log

from datetime import datetime
from flask import request, jsonify
from flask_restful import Resource, fields, marshal_with, abort

from clapton import db
from clapton.db.sqlalchemy import models

from clapton.api import types


LOG = log.getLogger(__name__)


class OrderList(Resource):
    def get(self):
        orders = db.get_session().query(models.Order).all()
        return jsonify((types.Order(many=True).dump(orders)).data), 200, {'X-Pagination-Total-Count': 1000}

        '''
        response = flask.make_response('[{"id": 123}]', 200)
        response.headers.extend({'X-Pagination-Total-Count': 1000,
                                 'Content-Type': 'application/json; charset=utf-8'})
        return response
        '''
        return [{"id": 123}], 200, {'X-Pagination-Total-Count': 1000}

    def post(self):
        '''
        validate request
        parser = reqparse.RequestParser()
        parser.add_argument(
            'total_amount',
            dest='total_amount',
            type=str,
            location='form',  # form, args, headers, cookies, json, files
            required=True,
            help='The orders\'s total amount',
        )
        args = parser.parse_args(strict=True)
        LOG.debug(args)
        LOG.debug(args.total_amount)
        return {}, 201
        '''
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No imput data provided'}), 400
        data, errors = types.Order().load(data)
        if errors:
            return jsonify(errors), 422
        o = models.Order(id=data['id'])
        return jsonify((types.Order().dump(o)).data), 201


class Order(Resource):
    @marshal_with({'id': fields.String, 'created_at': fields.DateTime, 'links': fields.Nested({'items': fields.Url('items', absolute=True)})})
    def get(self, order_id):
        '''
        outputing format
        '''
        return {'id': 123, 'created_at': datetime.now(), 'links': []}

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
