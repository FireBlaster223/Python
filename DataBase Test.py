from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TaskManager.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    tasks = db.relationship("Task", backref="user")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.now())

class CommonTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

db.create_all()

new_user = User(
    name="Lolicon Master",
    password="fullstack senior",
    username="Lucas"
)

new_task = Task(
    title="Lavar Louça",
    description="Lava prato lá mano",
    user_id=1
)

new_com_task = CommonTask(
    title="Limpar o Chão",
    description="Passa pano no chão mano"   
)

db.session.add_all([new_user, new_task, new_com_task])
db.session.commit()
