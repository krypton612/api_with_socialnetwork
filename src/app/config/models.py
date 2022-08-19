from flask_marshmallow import fields
from app import db, ma


class Users(db.Model):
    __tablename__ = "tb_users"
    id_user = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    age_user = db.Column(db.String(40), nullable=False)


class Notes(db.Model):

    __tablename__ = "tb_notes"
    id_note = db.Column(db.Integer(), primary_key=True, nullable=False)
    content = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.DateTime, server_default=db.func.now())
    id_user_fk = db.Column(db.Integer, db.ForeignKey('tb_users.id_user'))

class ModelUserView(ma.Schema): # mdoelo para crear el json que se devolvera luego de consultar a la db
    class Meta:
        fields = (
                "id_user",
                "name",
                "lastname",
                "email",
                "password",
                "age_user"
                )

class ModelNoteView(ma.Schema): # mdoelo para crear el json que se devolvera luego de consultar a la db
    class Meta:
        fields = (
                "id_note",
                "content",
                "fecha",
                "id_user_fk"
                )


class ModelRecyrclerView(ma.Schema): # mdoelo para crear el json que se devolvera luego de consultar a la db
    class Meta:
        fields = (
                "id_user",
                "name",
                "lastname",
                "email",
                "age_user",
                "content",
                "fecha"
                )


class ModelUserComment(ma.Schema): # mdoelo para crear el json que se devolvera luego de consultar a la db
    class Meta:
        fields = (
                "id_user",
                "name",
                "lastname",
                "email",
                "age_user",
                "content",
                "fecha"
                )


