from dataclasses import dataclass

from app.main.InstanciaEvaluativa import InstanciaEvaluativa


@dataclass
class EvaluacionFinal(InstanciaEvaluativa):
    tomo:str
    folio:str