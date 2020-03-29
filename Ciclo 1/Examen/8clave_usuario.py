clave = input("Ingrese Clave: ")
if len(clave) >= 8:
    for i in clave:
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            cumple1 = True
        elif i in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
            cumple2 = True
        elif i in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            cumple3 = True
        elif i in ["$","&"]:
            cumple4 = True
    if cumple1 and cumple2 and cumple3 and cumple4:
        print("Correcto")


else:
    print("Incorrecto")