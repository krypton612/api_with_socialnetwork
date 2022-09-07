from app.config.overide import create_note, create_user, delete_note, show_user, show_all_comment, show_user_comment, show_page,allpageCount, verify, show_all_user, verify_token_middleware, update_note, delete_note
from flask import Blueprint, request
from app.config.overide import login, validate_token

from app import app


routes_protected = Blueprint("routes_protected",__name__)
routes_not_protected = Blueprint("routes_not_protected",__name__)

routes_protected.before_request(verify_token_middleware)


routes_not_protected.add_url_rule("/api/create_user", 'create_user', create_user, methods=['POST'])
routes_protected.add_url_rule("/api/create_note", 'create_note', create_note, methods=['POST'])


routes_not_protected.add_url_rule("/api/user/<id_user>", 'show_user', show_user, methods=['GET'])

routes_not_protected.add_url_rule("/api/user/comment/<id_user>", 'show_user_comment', show_user_comment, methods=['GET'])



routes_not_protected.add_url_rule("/api/pages", 'show_page', show_page, methods=['GET'])

routes_not_protected.add_url_rule("/api/pages/allcount", 'allpageCount', allpageCount, methods=['GET'])

routes_not_protected.add_url_rule("/api/user/all", 'show_all_user', show_all_user, methods=['GET'])

routes_not_protected.add_url_rule("/api/user/comment/all", 'show_all_coment', show_all_comment, methods=['GET'])



# login app
routes_not_protected.add_url_rule("/api/login", "login", login, methods=['POST'])

routes_protected.add_url_rule("/api/verify/token", "verify", verify)




routes_not_protected.add_url_rule("/api/update_note/<id_user>", 'update_note', update_note, methods=['GET', "POST"])

routes_not_protected.add_url_rule("/api/delete_note", 'delete_note', delete_note, methods=['DELETE'])
