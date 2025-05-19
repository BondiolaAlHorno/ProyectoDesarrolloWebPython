from app.main.Docente import Docente
from app.main.Horario import Horario
from app.main.Materia import Materia
from dataclasses import dataclass

@dataclass
class MateriaImplementada():
    materia:Materia
    docente:Docente
    horario:[Horario]
    promocion:bool