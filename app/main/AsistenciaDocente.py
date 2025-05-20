from __future__ import annotations
from dataclasses import dataclass
from app.main.Asistencia import Asistencia


@dataclass
class AsistenciaDocente(Asistencia):
    horaIngreso:str
    horaSalida:str
    docente:Docente


from app.main.Docente import Docente