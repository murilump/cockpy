from cockpy import app, database, bcrypt
from cockpy.forms import FormLogin, FlaskForm
from cockpy.models import Usuario
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user

@app.route('/', methods=["POST", "GET"])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(usuario=form_login.usuario.data).first()
        if usuario and usuario.senha == form_login.senha.data:
            print("Logou")
            return redirect("home")
        else:
            print("Usuario ou senha incorreto")
            redirect(url_for("login"))
    return render_template("login.html", form=form_login)

@app.route("/home")
@login_required
def home():
    return render_template("home.html")