#funcion ejercicio 5

def categoria (time_reaction);
    if time_reaction<200:
        categoria='Rapido'
    elif time_reaction>500: 
        categoria='Lento'
    else:
        categoria='Normal'
    return categoria