class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.matriculas = []

    def matricular_en_programa(self, programa):
        matricula = Matricula(self, programa)
        self.matriculas.append(matricula)
        programa.matriculas.append(matricula)

    def __str__(self):
        return f"Empleado: {self.nombre} (ID: {self.id_empleado})"


class ProgramaCapacitacion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.matriculas = []

    def agregar_empleado(self, empleado):
        matricula = Matricula(empleado, self)
        empleado.matriculas.append(matricula)
        self.matriculas.append(matricula)

    def __str__(self):
        return f"Programa de Capacitación: {self.nombre}, Duración: {self.duracion} horas"


class Matricula:
    def __init__(self, empleado, programa):
        self.empleado = empleado
        self.programa = programa

    def __str__(self):
        return f"Matrícula:\nEmpleado: {self.empleado.nombre}\nPrograma de Capacitación: {self.programa.nombre}"


# Ejemplo de uso
empleado1 = Empleado("Juan", 1)
empleado2 = Empleado("Maria", 2)

programa1 = ProgramaCapacitacion("Python Básico", 20)
programa2 = ProgramaCapacitacion("Gestión de Proyectos", 30)
programa3 = ProgramaCapacitacion("Comunicación Efectiva", 15)

empleado1.matricular_en_programa(programa1)
empleado1.matricular_en_programa(programa2)
empleado2.matricular_en_programa(programa2)
empleado2.matricular_en_programa(programa3)

print("Matrículas de Empleado 1:")
for matricula in empleado1.matriculas:
    print(matricula)
print("\n")
print("Matrículas de Empleado 2:")
for matricula in empleado2.matriculas:
    print(matricula)
