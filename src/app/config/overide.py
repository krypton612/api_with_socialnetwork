from turtle import update
from urllib.request import Request
from warnings import catch_warnings
from flask import jsonify, request
from sqlalchemy.engine import result

from sqlalchemy import func
from app.config.auth import write_token, validate_token, expire_date

from app.config.models import ModelRecyrclerView, Users, Notes, Pages, ModelUserView, ModelNoteView, ModelUserComment, ModelPages, ModelCount, ModelLogin
from app import db, app


modelUser = ModelUserView()
modelUsers = ModelUserView(many=True)

modelNote = ModelNoteView()
modelNotes = ModelNoteView(many=True)

modelRecyrclerview = ModelRecyrclerView()
modelRecyrclerviews = ModelRecyrclerView(many=True)


modelUserComment = ModelUserComment()
modelUserComments = ModelUserComment(many=True)

modelPage = ModelPages()
modelPages = ModelPages(many=True)

modelCount = ModelCount(many=True)

modelLogin = ModelLogin(many=True)

locale = 0;


def create_user():

    register_fac = request.json

    user = Users(
            name=register_fac['name'],
            lastname=register_fac['lastname'],
            email=register_fac['email'],
            password=register_fac['password'],
            age_user=register_fac['age_user'],
            username=register_fac['username']
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
    # conteo de datos
    
    # select max(id_page) from tb_pages; debe de obtenerse y enviarse
    global locale
    
    maxPage = db.session.query(func.max(Pages.id_page));
    
    # suma 1 unidad a la tabla tb_pages
    page = Pages()
    # db.session.add(page)
    # db.session.commit()
    
    if locale <= 15:
        
        locale = locale + 1
        
    if locale == 15:
        db.session.add(page)
        db.session.commit()
        maxPage = db.session.query(func.max(Pages.id_page));
        locale = 1
        
    contenido = request.args.get('content')
    id_user_content = request.args.get('id')

    note = Notes(
            content=contenido,
            id_user_fk=id_user_content,
            id_page_fk=maxPage
            )
            
    notes = {"content": contenido, "id_user_fk": id_user_content}
    
    db.session.merge(note)
    db.session.commit()

    return jsonify(
            {
                "status": "OK",
                "message": "Publicacion Realizada",
                "dato": notes
            }
                ), 200



def update_note(id_user):
    # los espacios se representan como %20
    # http://127.0.0.1:5000/read_cars/search?name=MoiSes%20diaz
    contenido_actualizar = request.args.get('content')
    id_mostrar = request.args.get('id_note')
    pagin = request.args.get('page')



    if request.method == "POST":
        
        update_rows = Notes.query.get(id_mostrar)
        
        update_rows.content=contenido_actualizar
        notes2 = modelNote.dump(update_rows)
        
        db.session.commit()
        return jsonify({
                "status": "OK",
                "message": "Actualizacion exitosa",
                "dato": notes2
            }
                ), 200
    #  .order_by(Car.id_car.desc())
    user = db.session.query(
            Users.id_user,
            Users.name.label("name"),
            Users.lastname,
            Users.email,
            Users.age_user,
            Notes.content,
            Notes.id_page_fk.label("page")
            ).join(Users, Notes.id_user_fk == Users.id_user).filter(Users.id_user == id_user).filter(Notes.id_note == id_mostrar)

    datos = modelUserComments.dump(user)
    return jsonify({"STATUS": "OK", "data": datos})
    
    
    
def show_user(id_user):
    # los espacios se representan como %20
    # http://127.0.0.1:5000/read_cars/search?name=MoiSes%20diaz
    user = db.session.query(
            Users.id_user,
            Users.name.label("name"),
            Users.lastname,
            Users.username,
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
            Notes.content,
            Notes.id_note
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
            Users.username,
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
            Users.username,
            Users.age_user,
            )
    datos = modelUsers.dump(users)
    return jsonify({"STATUS": "OK", "data": datos}), 200


def show_page():
    pagina = request.args.get('page')
    users = db.session.query(
            Users.id_user,
            Users.name,
            Users.lastname,
            Users.email,
            Users.age_user,
            Users.username,
            Notes.content,
            Notes.fecha,
            Notes.id_page_fk
            ).join(Users, Notes.id_user_fk == Users.id_user).order_by(Notes.fecha.desc()).filter(Notes.id_page_fk == pagina)
    datos = modelPages.dump(users)
    return jsonify({"STATUS": "OK", "data": datos}), 200


def login():
    # data = request.get_json()
    username2 = request.args.get('username')
    password2 = request.args.get('password')
    
    
  
    # print(data['username'])
    # print(data['password'])
    try:   
       
        diccionario = {"username": username2, "password": password2}
        user = db.session.query(
                Users.id_user.label("id"),
                Users.username,
                Users.password,
                Users.age_user,
                Users.name,
                Users.lastname,
                Users.email
                ).filter(Users.username == username2 and Users.password == password2)
        
        userpassword = modelLogin.dump(user)
    
        username = userpassword[0]["username"]
        password = userpassword[0]["password"]
        
        
        token = write_token(diccionario)
        return jsonify({"STATUS": "OK", "data": userpassword, "token": token.decode("utf-8") })
        

    except Exception as e:
        print(e)
        response = jsonify({"message": "Contreña o usuario incorrectos"})
        response.status_code = 400
        return response

def verify():
    
    token = request.headers['Authorization'].split(" ")[1]

    return validate_token(token, output=True)

# desde aqui para abajo las rutas que requiren token.. /falsa alarma

def allpageCount():
    maxPage = db.session.query(
        
            Pages.id_page.label("CountPages")
        
            ).order_by(Pages.id_page.desc()).limit(1)
      
    datos = modelCount.dump(maxPage)
    
    return jsonify({"STATUS": "OK", "data": datos }), 200


def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)


def delete_note():
    id_note_rqe = request.args.get('id_note')
    Notes.query.filter_by(id_note=id_note_rqe).delete()
    db.session.commit()
    
    datos = {"datos": "Eliminados"}
    return datos