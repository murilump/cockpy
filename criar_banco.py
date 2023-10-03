from cockpy import database, app
from cockpy.models import Usuario, Servidor

with app.app_context():
    database.create_all()