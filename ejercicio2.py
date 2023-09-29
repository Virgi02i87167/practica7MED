#ejercicio 2
try:
    valor = int(input("Ingrese un numero: "))
    resultado = 10 / valor
except ValueError:
    print("Error: Debe ingresar un numero valido")
except ZeroDivisionError:
    print("Error: No se puede dividir entre 0")