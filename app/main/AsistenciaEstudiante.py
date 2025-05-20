from __future__ import annotations
from dataclasses import dataclass
from app.main.Asistencia import Asistencia


@dataclass
class AsistenciaEstudiante(Asistencia):
    estudiante:Estudiante



from app.main.Estudiante import Estudiante