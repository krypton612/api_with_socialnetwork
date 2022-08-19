from flask import jsonify, request
from app.config.models import ModelRecyrclerView, Users, Notes, ModelUserView, ModelNoteView, ModelUserComment
from app import db

modelUser = ModelUserView()
modelUsers = ModelUserView(many=True)

modelNote = ModelNoteView()
modelNotes = ModelNoteView(many=True)

modelRecyrclerview = ModelRecyrclerView()
modelRecyrclerviews = ModelRecyrclerView(many=True)


modelUserComment = ModelUserComment()
modelUserComments = ModelUserComment(many=True)


def create_user():

    register_fac = request.json

    user = Users(
            name=register_fac['name'],
            lastname=register_fac['lastname'],
            email=register_fac['email'],
            password=register_fac['password'],
            age_user=register_fac['age_user'],
            )

    db.session.add(user)
    db.session.commit()

    return jsonify(
            {
                "status": "OK",
                "message": "A sido agregado satisfactoriamente",
                "dato": register_fac
            }
                ), 200



def create_note():
    note_fac = request.json

    note = Notes(
            content=note_fac['content'],
            id_user_fk=note_fac['id_user_fk']
            )
            

    db.session.add(note)
    db.session.commit()

    return jsonify(
            {
                "status": "OK",
                "message": "A sido agregado satisfactoriamente",
                "dato": note_fac
            }
                ), 200




def show_user(id_user):
    # los espacios se representan como %20
    # http://127.0.0.1:5000/read_cars/search?name=MoiSes%20diaz
    user = db.session.query(
            Users.id_user,
            Users.name.label("name"),
            Users.lastname,
            Users.email,
            Users.age_user,
            ).filter(Users.id_user == id_user)

    #  .order_by(Car.id_car.desc())

    datos = modelUsers.dump(user)
    return jsonify({"STATUS": "OK", "data": datos})


def show_user_comment(id_user):
    # los espacios se representan como %20
    # http://127.0.0.1:5000/read_cars/search?name=MoiSes%20diaz
    user = db.session.query(
            Users.id_user,
            Users.name.label("name"),
            Users.lastname,
            Users.email,
            Users.age_user,
            Notes.content
            ).join(Users, Notes.id_user_fk == Users.id_user).filter(Users.id_user == id_user)

    #  .order_by(Car.id_car.desc())

    datos = modelUserComments.dump(user)
    return jsonify({"STATUS": "OK", "data": datos})

# muestra quienes hicieron un comentario


def show_all_comment():
    users = db.session.query(
            Users.id_user,
            Users.name,
            Users.lastname,
            Users.email,
            Users.age_user,
            Notes.content,
            Notes.fecha
            ).join(Users, Notes.id_user_fk == Users.id_user).order_by(Users.id_user.desc())
    datos = modelRecyrclerviews.dump(users)
    return jsonify({"STATUS": "OK", "data": datos}), 200


def show_all_user():
    users = db.session.query(
            Users.id_user,
            Users.name,
            Users.lastname,
            Users.email,
            Users.password,
            Users.age_user,
            )
    datos = modelUsers.dump(users)
    return jsonify({"STATUS": "OK", "data": datos}), 200
