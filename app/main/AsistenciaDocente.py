from dataclasses import dataclass

from app.main.Asistencia import Asistencia
from app.main.Docente import Docente


@dataclass
class AsistenciaDocente(Asistencia):
    horaIngreso:str
    horaSalida:str
    docente:Docente