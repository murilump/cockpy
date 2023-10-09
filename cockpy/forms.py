from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from cockpy.models import Usuario, Servidor, SistemaOperacional, Unidade, Responsavel

class FormLogin(FlaskForm):
    usuario = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_login = SubmitField("Entrar")

class FormAdicionarServidor(FlaskForm):
    hostname = StringField("Hostname", validators=[DataRequired()])
    ip = StringField("Hostname", validators=[DataRequired()])
    so = SelectField("Sistema Operacional", validators=[DataRequired()])
    funcao = StringField("Função", validators=[DataRequired()])
    responsavel = StringField("Responsável", validators=[DataRequired()])
    unidade = SelectField("Unidade", validators=[DataRequired()])
    botao_add = SubmitField("Adicionar")

