#Practica_8
#Realiza un programa para una calculadora

import os
os.system("cls")

#menu de opciones
print("---CALCULADORA---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Divicion")

#Entrada
opcion_calculadora=int(input("Elija una opcion: "))
numero1=int(input("Elija el segundo numero: "))
numero2=int(input("Elija el segundo numero: "))


#Proceso

match opcion_calculadora:
    case 1:
        print("Operacion de suma")
        resultado=numero1+numero2
        print(f"la suma es: {resultado}")
    case 2:
        print("Operacion de resta")
        resultado=numero1-numero2
        print(f"la resta es: {resultado}")
    case 3:
        print("Operacion de Multiplicacion")
        resultado=numero1*numero2
        print(f"la Multiplicacion es: {resultado}")
    case 4:
        print("Operacion de Divicion")
        resultado=numero1/numero2
        print(f"la Divicion  es: {resultado}")
    case _:
        print("Error, seleccione nuevamente")
print("Gracias por usar mi calculadora")
     
