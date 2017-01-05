from marshmallow import Schema, fields


class Order(Schema):
    id = fields.Int(dump_only=True)
    items = fields.Nested('OrderItem')


class OrderItem(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(dump_only=True)
