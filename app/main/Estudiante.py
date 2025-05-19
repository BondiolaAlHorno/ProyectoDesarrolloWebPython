from dataclasses import dataclass
from app.main.Persona import Persona

@dataclass
class Estudiante(Persona):
    carreras:[Carrera]