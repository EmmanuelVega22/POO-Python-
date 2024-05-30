class GestorEmpleados:
    def __init__(self):
        self.lista_empleados = []

    def registrar_empleado(self, empleado):
        self.lista_empleados.append(empleado)

class GestorProgramaCapacitacion:
    def __init__(self):
        self.lista_programas = []

    def registrar_programa(self, programa):
        self.lista_programas.append(programa)

class GestorMatricula:
    def __init__(self):
        self.lista_matriculas = []

    def matricular_empleado_en_programa(self, empleado, programa):
        matricula = Matricula(empleado, programa)
        empleado.matriculas.append(matricula)
        programa.matriculas.append(matricula)
        self.lista_matriculas.append(matricula)

# Ejemplo de uso
gestor_empleados = GestorEmpleados()
gestor_programas = GestorProgramaCapacitacion()
gestor_matriculas = GestorMatricula()

empleado1 = Empleado("Juan", "González", 1, "Desarrollador")
empleado2 = Empleado("Maria", "Lopez", 2, "Gerente")

programa1 = ProgramaCapacitacion("Python Básico", "PC001", 20)
programa2 = ProgramaCapacitacion("Gestión de Proyectos", "PC002", 30)

gestor_empleados.registrar_empleado(empleado1)
gestor_empleados.registrar_empleado(empleado2)

gestor_programas.registrar_programa(programa1)
gestor_programas.registrar_programa(programa2)

gestor_matriculas.matricular_empleado_en_programa(empleado1, programa1)
gestor_matriculas.matricular_empleado_en_programa(empleado1, programa2)
