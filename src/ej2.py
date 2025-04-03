#funcion del ejercicio 2 
def titulo_mas_largo (titles):
    max=0 #variable contador en cero
    for title in titles:
        if len(title)>max:
            max=len(title) #actualizo el contador con el nuevo max
            max_title=title #actualizo el titulo mas largo
    return max_title #devuelvo el titulo mas largo