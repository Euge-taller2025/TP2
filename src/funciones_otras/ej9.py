
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
    


#funcion principal
def cleaner (clients):
    cleaned_list=[]
    for data in clients:
        name_cleaned=clean_space(data)
        if name_cleaned: #si no es vacio
            name_cleaned= conv_title (name_cleaned)
            cleaned_list.append (name_cleaned)
    return cleaned_list