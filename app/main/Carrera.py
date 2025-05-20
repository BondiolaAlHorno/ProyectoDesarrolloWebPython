from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Carrera:
    nombre:str
    materias:List[Materia]
    duracion:int

    def agregarMateria(self,materia:Materia):
        self.materias.append(materia)

from app.main.Materia import Materia