from __future__ import annotations
from dataclasses import dataclass
from typing import List
from app.main.Persona import Persona


@dataclass
class Estudiante(Persona):
    carreras:List[Carrera]

    def agregarMateria(self,carrera:Carrera):
        self.carreras.append(carrera)


from app.main.Carrera import Carrera