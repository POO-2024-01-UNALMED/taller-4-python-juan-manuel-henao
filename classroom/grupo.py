from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        if asignaturas is None:
            asignaturas=[]
        if estudiantes is None:
            estudiantes=[]
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        Grupo.grado="Grado 12"

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))
    
   
    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista=[]
        lista.append(alumno)
        for i in lista:
            self.listadoAlumnos.append(i)
    
    def __str__(self):
        texto="Grupo de estudiantes: "+self._grupo
        return texto

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre