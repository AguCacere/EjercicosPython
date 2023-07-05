n1 = float(input("Ingrese el numero 1: "))
n2 = float(input("Ingrese numero 2:" ))
print("1, suma")
print("2, resta")
print("3, multiplcacion")
print("4, division")
print("5, exponenciacion")
print("6, radicacion")


opc = int(input("Ingrese la opcion que desea: "))

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def divison(a, b):
    return a / b
def expo(a, b):
    return a ** b
def raiz(a, b):
    return a ** (1/b)

if opc == 1:
    print(n1, "+", n2, "=", suma(n1,n2))
elif opc == 2:
    print(n1, "-", n2, "=", resta(n1,n2))
elif opc == 3:
    print(n1, "*", n2, "=", multiplicacion(n1,n2))
elif opc == 4:
    print(n1, "/", n2, "=", divison(n1,n2))
elif opc == 5:
    print(n1, "^", n2, "=", expo(n1,n2))
elif opc == 6:
    print(n1, "^ 1/", n2, "=", raiz(n1,n2))
else:
    print("Error, ingresar un dato correspondiente")





    
