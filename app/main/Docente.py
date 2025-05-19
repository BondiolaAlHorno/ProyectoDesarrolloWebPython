from app.main.Asistencia import Asistencia
from app.main.MateriaImplementada import MateriaImplementada
from app.main.Persona import Persona
from dataclasses import dataclass

@dataclass
class Docente(Persona):
    legajo:int
    asistencia:[Asistencia]
    materias:[MateriaImplementada]

