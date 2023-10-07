from cockpy import app, database, bcrypt
from cockpy.forms import FormLogin, FlaskForm
from cockpy.models import Usuario, Servidor
from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user

@app.route('/', methods=["POST", "GET"])
def login():
    form_login = FormLogin()
    usuario = Usuario.query.filter_by(usuario=form_login.usuario.data).first()
    print(current_user)
    if form_login.validate_on_submit():
        if usuario and usuario.senha == form_login.senha.data:
            login_user(usuario, remember=True)
            print("Logou")
            return redirect("home")
        else:
            print("Usuario ou senha incorreto")
    return render_template("login.html", form=form_login)

@app.route("/home")
@login_required
def home():
    servidores = Servidor.query.all()[:10]
    return render_template("home.html", servidores=servidores)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login")) 

@app.route("/exemplo")
def exemplo():
    return render_template("exemplo.html")