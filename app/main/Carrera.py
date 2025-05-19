from dataclasses import dataclass

from app.main.Materia import Materia


@dataclass
class Carrera:
    nombre:str
    materias:[Materia]
    duracion:int