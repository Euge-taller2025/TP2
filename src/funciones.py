
#funcion del ejercicio 1 
def vocales_in_zen (zen_text):
    lines=zen_text.splitlines("\n") #divido el texto en lineas, se genera una lista
    vocales="AEIOUaeiou"
    for line in lines:
        words= line.split() #divido la linea en palabras, se genera otra lista
        if len(words)>1 and words [1][0] in vocales: #si la linea tiene mas de una palabra y la segunda empieza con vocal (words[1][0] hace referencia a la primer letra))
            print (line)


