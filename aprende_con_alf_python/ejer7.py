peso = float(input("Ingrese el peso(KG): "))
altura = float(input("Ingrese la altura(M): "))
IMC = round((peso / altura) **2,2)

print("Tu indice de msa muscular es de " + str(IMC))
