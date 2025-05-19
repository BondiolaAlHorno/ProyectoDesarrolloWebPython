from dataclasses import dataclass

from app.main.Estudiante import Estudiante
from app.main.EvaluacionFinal import EvaluacionFinal
from app.main.InstanciaEvaluativa import InstanciaEvaluativa
from app.main.MateriaImplementada import MateriaImplementada


@dataclass
class MateriaEstudiante:
    estudiante:Estudiante
    materia:MateriaImplementada
    evaluaciones:[InstanciaEvaluativa]
    evalucaionFinal:EvaluacionFinal
    estadoPromocion:bool
    estadoCursada:bool
    equivalencia:bool