comprobar = True

while comprobar ==True:
    n = int(input("Ingrese un numero positivo: "))
    if n > 0:
        for i in range(1, 11):
            print(n, "por", i, "es igual a", n*i)
        comprobar = False
    else:
        print("ERROR: Ingrese un numero positivo")
    
    

