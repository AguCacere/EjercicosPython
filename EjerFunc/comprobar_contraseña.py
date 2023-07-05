def comprobar_contraseña(contraseña):
    largo = False
    mayuscula = False
    numero = False
    if len(contraseña) > 8:
        largo = True
    for i in range(len(contraseña)):
        if contraseña[i].isupper():
            mayuscula = True
        if contraseña[i].isnumeric():
            numero = True
    if largo and mayuscula and numero:
        return True
    else: 
        return False
contraseña = input("Ingresa su contraseña")
verificacion = comprobar_contraseña(contraseña)
if verificacion:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")
