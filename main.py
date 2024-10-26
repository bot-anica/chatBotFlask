from app import app, db
from app.models import User, Chat, Message


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Chat=Chat, Message=Message)
