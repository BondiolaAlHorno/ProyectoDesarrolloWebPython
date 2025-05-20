from __future__ import annotations
from typing import List
from dataclasses import dataclass
from app.main.Persona import Persona

@dataclass
class Docente(Persona):
    legajo:int
    asistencia:List[Asistencia]
    materias:List[MateriaImplementada]

from app.main.Asistencia import Asistencia
from app.main.MateriaImplementada import MateriaImplementada