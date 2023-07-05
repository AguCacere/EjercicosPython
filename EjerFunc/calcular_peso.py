peso = float(input("Ingrese el peso(kg): "))
altura = float(input("Ingrese la estatura(m): "))
def calcular_IMC(P, A):
    return P / (A* A)

def nivel_peso(IMC):
    if IMC > 18.5:
        return "Bajo peso"
    elif IMC >= 24.9:
        return "Peso normal"
    elif IMC >= 29.9:
        return "Sobre peso"
    elif IMC >= 34.9:
        return "Obesidad I"
    elif IMC >= 39.9:
        return "Obesidad II"
    elif IMC >= 49.9:
        return "Obesidad III"
    elif IMC >= 50.0:
        return "Obesidad IIII"

print("Su nivel de peso es: ", nivel_peso(calcular_IMC(peso, altura)))

    





