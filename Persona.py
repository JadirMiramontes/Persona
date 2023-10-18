import random

class Persona:
    SEXO_HOMBRE = 'H'
    SEXO_MUJER = 'M'

    def __init__(self, nombre="", edad=0, sexo=SEXO_HOMBRE, peso=0.0, altura=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = self.generaDNI()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    def calcularIMC(self):
        if self.__altura == 0:
            return -1
        imc = self.__peso / (self.__altura ** 2)
        if imc < 20:
            return -1
        elif 20 <= imc <= 25:
            return 0
        else:
            return 1

    def esMayorDeEdad(self):
        return self.__edad >= 18

    def comprobarSexo(self, sexo):
        return sexo == self.SEXO_HOMBRE or sexo == self.SEXO_MUJER

    def toString(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nDNI: {self.__dni}\nSexo: {self.__sexo}\nPeso: {self.__peso} kg\nAltura: {self.__altura} m"

    def generaDNI(self):
        dni_numero = random.randint(10000000, 99999999)
        letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        letra = letras[dni_numero % 23]
        return f"{dni_numero}-{letra.upper()}"

    # Métodos set
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad

    def setSexo(self, sexo):
        if self.comprobarSexo(sexo==""):
            self.__sexo = self.SEXO_HOMBRE
        elif self.comprobarSexo(sexo):
            self.__sexo = sexo

    def setPeso(self, peso):
        self.__peso = peso

    def setAltura(self, altura):
        self.__altura = altura

# Clase ejecutable
def main():
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))
    sexo = input("Introduce el sexo (H para hombre, M para mujer): ").upper()
    peso = float(input("Introduce el peso en kg: "))
    altura = float(input("Introduce la altura en metros: "))

    persona1 = Persona(nombre, edad,sexo, peso, altura)
    persona2 = Persona(nombre, edad)
    persona3 = Persona()

    persona2.setPeso(75.5)
    persona2.setAltura(1.75)

    persona3.generaDNI()

    persona3.setNombre(nombre)
    persona3.setEdad(edad)
    persona3.setPeso(round(random.uniform(200,30)))
    persona3.setAltura(round(random.uniform(2.99,1.01),2))

    personas = [persona1, persona2, persona3]

    for i, persona in enumerate(personas):
        print(f"\nInformación de la Persona {i + 1}:")
        print(persona.toString())
        resultado_imc = persona.calcularIMC()
        if resultado_imc == -1:
            print("La persona está por debajo de su peso ideal.")
        elif resultado_imc == 0:
            print("La persona está en su peso ideal.")
        else:
            print("La persona tiene sobrepeso.")
        if persona.esMayorDeEdad():
            print("La persona es mayor de edad.")
        else:
            print("La persona es menor de edad.")

if __name__ == "__main__":
    main()