import db
from sqlalchemy import Column, Integer, String, Boolean

class Tarea(db.Base):

    __tablename__ = "Tarea"

    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    fecha = Column(String)
    hoy = Column(String)

    def __init__(self, contenido, hecha, fecha, hoy):

        self.contenido = contenido
        self.hecha = hecha
        self.fecha = fecha
        self.hoy = hoy


    def __str__(self):

        return "{}: {}, {}".format(self.contenido, self.hecha, self.fecha)