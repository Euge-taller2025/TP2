#funcion ejercicio 7
import random
import string

def generador_descuento (usuario,today):
    codigo=usuario.upper() + "-" +str(today.year)+ str(today.month)+ str(today.day)
    letra_mayus_y_num =string.ascii_uppercase + string.digits
    max=30
    cant= max - len (codigo)-1
    codigo= codigo + "-" + "".join(random.choices(letra_mayus_y_num, k=cant))
    return codigo