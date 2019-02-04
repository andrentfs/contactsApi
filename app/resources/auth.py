import datetime

import jwt
from flask_restful import Resource, marshal

from app import db, request, app
from app.models import User
from app.schemas import users_fields


class LoginRouter(Resource):
    def post(self):
        credential = request.only(["username", "password"])

        user = User.query.filter_by(username=credential["username"]).first()

        if not user or not user.compare_password(credential["password"]):
            return {"error": "Credenciais inválida."}, 400

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }

        try:
            token = jwt.encode(payload, app.config["SECRET_KEY"])
            return {"token": token.decode("utf-8")}
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500


class RegisterRouter(Resource):
    def post(self):
        credential = request.only(["username", "password"])

        try:
            user = User(credential["username"], credential["password"])
            db.session.add(user)
            db.session.commit()
            return marshal(user, users_fields, "user")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500
