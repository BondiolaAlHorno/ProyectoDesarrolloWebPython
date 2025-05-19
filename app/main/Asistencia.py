from dataclasses import dataclass
from datetime import date

from app.main.Estudiante import Estudiante
from app.main.MateriaImplementada import MateriaImplementada


@dataclass
class Asistencia:
    fecha:date
    asistencia:str
    materia:MateriaImplementada
    estudiante:Estudiante