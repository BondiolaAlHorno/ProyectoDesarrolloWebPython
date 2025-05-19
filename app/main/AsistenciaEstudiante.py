from dataclasses import dataclass

from app.main.Asistencia import Asistencia
from app.main.Estudiante import Estudiante


@dataclass
class AsistenciaEstudiante(Asistencia):
    estudiante:Estudiante