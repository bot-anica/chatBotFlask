from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


def lazy_utc_now():
    return datetime.now(tz=timezone.utc)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    chats = db.relationship('Chat', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    messages = db.relationship('Message', backref='related_chat', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Chat {self.id}>'


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), default='user')
    text = db.Column(db.String(1024), index=True)
    emotion = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, index=True, default=lazy_utc_now)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))

    def __repr__(self):
        return f'<Message {self.text}>'
