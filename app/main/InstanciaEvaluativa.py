from dataclasses import dataclass
from datetime import date

from app.main.Estudiante import Estudiante
from app.main.MateriaImplementada import MateriaImplementada


@dataclass
class InstanciaEvaluativa:
    estudiante:Estudiante
    fecha:date
    nota:float
    materia:MateriaImplementada