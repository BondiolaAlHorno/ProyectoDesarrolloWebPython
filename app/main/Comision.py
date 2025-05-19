from dataclasses import dataclass

from app.main.Carrera import Carrera
from app.main.Estudiante import Estudiante
from app.main.MateriaImplementada import MateriaImplementada


@dataclass
class Comision:
    materias:[MateriaImplementada]
    carreras:Carrera
    estudiantes:[Estudiante]
    turno:str
    nombre:str