from flask_restful import Resource, marshal
from app.models import Contact
from app.schemas import contacts_fields
from app import request, db
from app.decorator import jwt_required



class ContactRouter(Resource):
    def get(self):
        contacts = Contact.query.all()
        return marshal(contacts, contacts_fields, "contacts")

    @jwt_required
    def post(self, current_user):
        credential = request.only(["name", "cellphone"])

        try:
            contact = Contact(credential["name"], credential["cellphone"])
            db.session.add(contact)
            db.session.commit()
            return marshal(contact, contacts_fields, "contact")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500
    
    @jwt_required
    def delete(self, current_user):
        credential = request.only(["id"])
        contact = Contact.query.get(credential["id"])

        if not contact:
            return {"error": "Contato não existe!"}
        
        try:
            db.session.delete(contact)
            db.session.commit()
            return marshal(contact, contacts_fields, "contact")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500

    @jwt_required
    def put(self, current_user):
        credential = request.only(["id", "name", "cellphone"])
        contact = Contact.query.get(credential["id"])
        
        if not contact:
            return {"error": "Contato não existe!"}

        try:
            contact.name = credential["name"]
            contact.cellphone = credential["cellphone"]
            db.session.add(contact)
            db.session.commit()
            return marshal(contact, contacts_fields, "contact")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500