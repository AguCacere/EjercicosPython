dias = int(input("Ingrese la cantidad de dias: "))
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))

def calcular_segundos(d, h, m, s):
    segundos_totales = 0
    segundos_totales =+ s
    segundos_totales =+ m * 60
    segundos_totales =+ h * 60 * 60
    segundos_totales =+ d * 24 * 60 * 60
    return segundos_totales

segundos_totales = calcular_segundos(dias, horas, minutos, segundos)
print("La cantidad de segundos totales es: ", segundos_totales)


    

