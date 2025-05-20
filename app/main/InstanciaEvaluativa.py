from __future__ import annotations
from dataclasses import dataclass
from datetime import date


@dataclass
class InstanciaEvaluativa:
    estudiante:Estudiante
    fecha:date
    nota:float
    materia:MateriaImplementada


from app.main.Estudiante import Estudiante
from app.main.MateriaImplementada import MateriaImplementada