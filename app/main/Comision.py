from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Comision:
    materias: List[MateriaImplementada]
    carreras:Carrera
    estudiantes:List[Estudiante]
    turno:str
    nombre:str


from app.main.Carrera import Carrera
from app.main.Estudiante import Estudiante
from app.main.MateriaImplementada import MateriaImplementada