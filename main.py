from flask import *
import db
from models import Tarea
from datetime import date

# inicializar el servidor en el dominio actual
app = Flask(__name__)



@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    #for i in todas_las_tareas:
        #print(i)

    return render_template("index.html", lista_tareas = todas_las_tareas)

@app.route('/crear', methods=["POST"])
def crear():

    tarea = Tarea(contenido=request.form["tarea"], hecha=False, fecha=request.form["fecha"], hoy=d1)
    db.session.add(tarea)
    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))

@app.route('/eliminar/<id>')
def eliminar(id):

    tarea = db.session.query(Tarea).filter_by(id=id).delete()
    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))

@app.route('/hecho/<id>')
def hecho(id):

    tarea = db.session.query(Tarea).filter_by(id=id).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))

today = date.today()
d1 = today.strftime("%Y-%m-%d")

# el codigo empieza por la carpeta main.py

if __name__ == "__main__":

    db.Base.metadata.create_all(db.enginge) #creamos el modelo de datos

    # arranca el servidor web
    app.run(host="0.0.0.0", port=8000, debug=True)

