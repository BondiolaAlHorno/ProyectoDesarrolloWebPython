from __future__ import annotations
from dataclasses import dataclass
from datetime import date


@dataclass
class Asistencia:
    fecha:date
    asistencia:str
    materia:MateriaImplementada
    estudiante:Estudiante


from app.main.Estudiante import Estudiante
from app.main.MateriaImplementada import MateriaImplementada