from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class MateriaEstudiante:
    estudiante:Estudiante
    materia:MateriaImplementada
    evaluaciones:List[InstanciaEvaluativa]
    evalucaionFinal:EvaluacionFinal
    estadoPromocion:bool
    estadoCursada:bool
    equivalencia:bool


from app.main.Estudiante import Estudiante
from app.main.EvaluacionFinal import EvaluacionFinal
from app.main.InstanciaEvaluativa import InstanciaEvaluativa
from app.main.MateriaImplementada import MateriaImplementada