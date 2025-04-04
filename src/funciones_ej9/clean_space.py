def clean_space (name):
    if name: #si el elemento no es vacio
        name=name.strip () #elimina los espacios al inicio y al final
        return name
    else:
        return None