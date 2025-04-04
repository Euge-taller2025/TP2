#funcion del ejercicio 3

def search_rule (rules, clave):
    lines=rules.splitlines("\n") #divido el texto en lineas, se genera una lista
    for line in lines:
        words= line.split() #divido la linea en palabras, se genera otra lista
        for word in words:
            if clave in word:
                print (line)