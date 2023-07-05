salario_actual = float(input("Ingrese el salario actual: "))
incremento = float(input("Ingrese el incremento: "))

def calcular_incremento(salario, x):
    nuevo_salario = salario + (salario*(x/100))
    return nuevo_salario

salario_nuevo = calcular_incremento(salario_actual, incremento)
print("El nuevo salario del trabajor es: ", salario_nuevo)
