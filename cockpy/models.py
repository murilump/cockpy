from cockpy import database
from flask_login import UserMixin

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    usuario = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    role = database.Column(database.String, nullable=False)

class Servidor(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    hostname = database.Column(database.String, nullable=False, unique=True)
    ip = database.Column(database.String, nullable=False, unique=True)
    so = database.Column(database.String, nullable=False)
    funcao = database.Column(database.String, nullable=False)
    responsavel = database.Column(database.String, nullable=False)
    unidade = database.Column(database.String, nullable=False)
