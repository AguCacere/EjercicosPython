palabra = input("Ingrese la palabra: ")

def es_palindromo(p):
    p = p.lower()
    p = p.replace(" ", "")
    p = p.replace("á","a")
    p = p.replace("é","e")
    p = p.replace("í","i")
    p = p.replace("ó","o")
    p = p.replace("ú","u")
    
    a = 0
    b = len(p) - 1
    
    for i in range(0, len(p)):
        if p[a] == p[b]:
            a += 1
            b += 1
        else:
            return False
    return True

print(es_palindromo(palabra))


    