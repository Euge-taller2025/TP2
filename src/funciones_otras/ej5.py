#funcion ejercicio 5

def categoria (time_reaction):
    if time_reaction<200:
        tipo='Rapido'
    elif time_reaction>500: 
        tipo='Lento'
    else:
        tipo='Normal'
    return tipo