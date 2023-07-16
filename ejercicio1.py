class Persona:
    def __init__(self):
        self.__nombre = input("Por favor, introduce tu nombre: ")
        self.edad = int(input("Por favor, introduce tu edad: "))
        self.ciudad = input("Por favor, introduce tu ciudad: ")

    def imprimir_datos(self):
        return f'Nombre: {self.__nombre}, Edad: {self.edad}, Ciudad: {self.ciudad}'

    def get_nombre(self):
        return self.__nombre


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Por favor, introduce tu sueldo: "))
        self.impuesto = self.calcular_impuesto()

    def calcular_impuesto(self):
        if self.sueldo > 5500:
            return self.sueldo * 0.09
        else:
            return 0

    def manejoDiccionario(self):
        return {
            'nombre': self.get_nombre(),
            'edad': self.edad,
            'ciudad': self.ciudad,
            'sueldo': self.sueldo,
            'impuesto': self.impuesto
        }

    def generarArchivoEmpleado(self):
        with open('empleados.txt', 'a') as f:
            f.write(f"{self.get_nombre()},{self.sueldo},{self.impuesto}\n")

    @staticmethod
    def mostrarEmpleados():
        with open('empleados.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())


def main():
    empleado1 = Empleado()
    print(empleado1.imprimir_datos())
    print(empleado1.manejoDiccionario())
    empleado1.generarArchivoEmpleado()

    empleado2 = Empleado()
    print(empleado2.imprimir_datos())
    print(empleado2.manejoDiccionario())
    empleado2.generarArchivoEmpleado()

    Empleado.mostrarEmpleados()


if __name__ == "__main__":
    main()
