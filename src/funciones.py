
#funcion del ejercicio 1
def vocales_in_zen (zen_text):
    lines=zen_text.splitlines("\n") #divido el texto en lineas, se genera una lista
    vocales="AEIOUaeiou"
    for line in lines:
        words= line.split() #divido la linea en palabras, se genera otra lista
        if len(words)>1 and words [1][0] in vocales: #si la linea tiene mas de una palabra y la segunda empieza con vocal (words[1][0] hace referencia a la primer letra))
            print (line)


#funcion del ejercicio 2 
def titulo_mas_largo (titles):
    max=0 #variable contador en cero
    for title in titles:
        if len(title)>max:
            max=len(title) #actualizo el contador con el nuevo max
            max_title=title #actualizo el titulo mas largo
    return max_title #devuelvo el titulo mas largo