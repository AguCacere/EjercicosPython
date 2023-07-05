inversion_inicial = float(input("Ingrese capital a invertir: "))
intereses = float(input("interes anual? "))
años = int(input("Cuantos años? "))

print("El capital final es de: ", str(round(inversion_inicial * (intereses / 100 + 1)**años, 2)))

