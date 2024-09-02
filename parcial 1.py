class Persona:
    def __init__(self, nombre: str, apellido: str, direccion: str, telefono: str, edad: int, email: str):
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._telefono = telefono
        self._edad = edad
        self._email = email

    
    def nombre(self) -> str:
        return self._nombre

    
    def nombre(self, nombre: str):
        self._nombre = nombre

    
    def apellido(self) -> str:
        return self._apellido

    
    def apellido(self, apellido: str):
        self._apellido = apellido

    
    def direccion(self) -> str:
        return self._direccion

    
    def direccion(self, direccion: str):
        self._direccion = direccion

    
    def telefono(self) -> str:
        return self._telefono

    
    def telefono(self, telefono: str):
        self._telefono = telefono

    
    def edad(self) -> int:
        return self._edad

    
    def edad(self, edad: int):
        self._edad = edad

    def email(self) -> str:
        return self._email

    
    def email(self, email: str):
        self._email = email

class Empleado(Persona):
    def __init__(self, nombre: str, apellido: str, direccion: str, telefono: str, edad: int, email: str,
                 salario: float, jefe_inmediato: str, años_experiencia: int):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self._salario = salario
        self._jefe_inmediato = jefe_inmediato
        self._años_experiencia = años_experiencia
        self._cargo = self._determinar_cargo()

    
    def salario(self) -> float:
        return self._salario

    
    def salario(self, salario: float):
        self._salario = salario
        self._cargo = self._determinar_cargo()

    
    def jefe_inmediato(self) -> str:
        return self._jefe_inmediato

    
    def jefe_inmediato(self, jefe_inmediato: str):
        self._jefe_inmediato = jefe_inmediato


    def años_experiencia(self) -> int:
        return self._años_experiencia

    
    def años_experiencia(self, años_experiencia: int):
        self._años_experiencia = años_experiencia
        self._cargo = self._determinar_cargo()

    
    def cargo(self) -> str:
        return self._cargo

    def _determinar_cargo(self) -> str:
        if self._salario >= 5000000 and self._años_experiencia >= 5 and 25 <= self._edad <= 45:
            return "Senior"
        elif 900000 <= self._salario <= 1200000 and 1 <= self._años_experiencia <= 2 and 18 <= self._edad <= 22:
            return "Junior"
        else:
            return "No definido"

    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Edad: {self.edad}")
        print(f"Email: {self.email}")
        print(f"Salario: {self.salario}")
        print(f"Jefe Inmediato: {self.jefe_inmediato}")
        print(f"Años de Experiencia: {self.años_experiencia}")
        print(f"Cargo: {self.cargo}")

def main():
    print("Ingrese los datos del empleado:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    edad = int(input("Edad: "))
    email = input("Email: ")
    salario = float(input("Salario: "))
    jefe_inmediato = input("Jefe Inmediato: ")
    años_experiencia = int(input("Años de Experiencia: "))

    empleado = Empleado(nombre, apellido, direccion, telefono, edad, email, salario, jefe_inmediato, años_experiencia)
    empleado.mostrar_detalle()

if __name__ == "__main__":
    main()

    