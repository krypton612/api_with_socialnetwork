from app.config.overide import create_note, create_user, show_user, show_all_user, show_all_comment, show_user_comment
from app import app


app.add_url_rule("/api/create_user", 'create_user', create_user, methods=['POST'])
app.add_url_rule("/api/create_note", 'create_note', create_note, methods=['POST'])


app.add_url_rule("/api/user/<id_user>", 'show_user', show_user, methods=['GET'])
app.add_url_rule("/api/user/comment/<id_user>", 'show_user_comment', show_user_comment, methods=['GET'])


app.add_url_rule("/api/user/all", 'show_all_user', show_all_user, methods=['GET'])

app.add_url_rule("/api/user/comment/all", 'show_all_coment', show_all_comment, methods=['GET'])



