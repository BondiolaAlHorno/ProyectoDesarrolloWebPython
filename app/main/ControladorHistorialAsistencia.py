from __future__ import annotations
from datetime import date
from typing import List
from app.main.Asistencia import Asistencia
from app.main.Estudiante import Estudiante
from app.main.MateriaImplementada import MateriaImplementada


class ControladorHistorialAsistencia:
    pass

    # @staticmethod
    # def recuperarListadoMateriasCursadas(self)->List[MateriaImplementada]:
    #     return

    @staticmethod
    def recuperarListadoDeFechas(self,listaAsistencia:List[Asistencia])->date:
        listaFecha: List[date]=[]
        for asistencia in listaAsistencia:
            listaFecha.append(asistencia.fecha)
        return  listaFecha

    @staticmethod
    def recuperarListadoAsistenciaPorMateria(self,listaAsistencia:List[Asistencia],materia:MateriaImplementada)->List[Asistencia]:
        asistencias: List[Asistencia] = []
        for asistencia in listaAsistencia:
            if materia == asistencia.materia:
                asistencias.append(asistencia)
        return asistencias

    @staticmethod
    def recuperarListadoAsistenciaPorFecha(self,listaAsistencia:List[Asistencia],fecha:date)->List[Asistencia]:
        asistencias: List[Asistencia] = []
        for asistencia in listaAsistencia:
            if fecha == asistencia.fecha:
                asistencias.append(asistencia)
        return asistencias

    @staticmethod
    def recuperarListadoAsistenciaPorEstudiante(self,listaAsistencia:List[Asistencia],estudiante:Estudiante)->List[Asistencia]:
        asistencias: List[Asistencia] = []
        for asistencia in listaAsistencia:
            if estudiante == asistencia.estudiante:
                asistencias.append(asistencia)
        return asistencias

    @staticmethod
    def recuperarPorcentajeDeAsistencia(self,listaAsistencia:List[Asistencia])->float:
        presentes:float = 0.0
        for asistencia in listaAsistencia:
            if asistencia.asistencia == "P" or asistencia.asistencia == "J":
                presentes+=1
        porcentaje = ((presentes/listaAsistencia.len())*100.0)
        return porcentaje