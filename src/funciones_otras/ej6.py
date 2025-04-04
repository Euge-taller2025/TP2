#funcion del ejercicio 6

def menciones (tipo,text):
    cont=0
    for line in text:
        words= line.split()
        for word in words:
            if word.lower()==tipo:
                cont+=1
    return cont
        