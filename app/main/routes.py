from flask_login import login_required

from app.main import bp, controllers


@bp.context_processor
def inject_chats():
    return controllers.inject_chats()


@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return controllers.index()


@bp.route('/chat/<chat_id>', methods=['GET', 'POST'])
@login_required
def chat(chat_id):
    return controllers.chat(chat_id)
