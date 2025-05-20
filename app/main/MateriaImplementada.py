from __future__ import annotations
from typing import List
from dataclasses import dataclass


@dataclass
class MateriaImplementada():
    materia:Materia
    docente:Docente
    horario:List[Horario]
    promocion:bool
    comision:Comision


from app.main.Comision import Comision
from app.main.Docente import Docente
from app.main.Horario import Horario
from app.main.Materia import Materia