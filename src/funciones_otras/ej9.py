
#limpia espacios extra
def clean_space (name):
    if name: #si el elemento no es vacio
        name=name.strip () #elimina los espacios al inicio y al final
        return name
    else:
        return None

#convierte a formato titulo
def conv_title (name):
    if name:
        name=name.title()
        return name
    else:
        return None
    
#elimina duplicados
def delete_dupl (cleaned_list):
    cleaned_list= dict.fromkeys (cleaned_list) #diccionario con las claves de la lista (sin repetir)
    return list(cleaned_list) #convierto el dicc en una lista nuevamente


#funcion principal
def cleaner (clients):
    cleaned_list=[]
    for data in clients:
        name_cleaned=clean_space(data)
        if name_cleaned: #si no es vacio (aca elimino valores nulos)
            name_cleaned= conv_title (name_cleaned)
            cleaned_list.append (name_cleaned)
    cleaned_list=delete_dupl(cleaned_list)
    return sorted(cleaned_list,key=None) #devuelvo la lista limpia y ordenada