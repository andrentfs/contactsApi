from flask_restful import fields


users_fields = {
    "id": fields.Integer,
    "username": fields.String
}

contacts_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "cellphone": fields.String,
}