import clean_space, conv_title

def cleaner (clients):
    list=[]
    for data in clients:
        name_cleaned=clean_space(data)
        if name_cleaned: #si no es vacio
            name_cleaned= conv_title (name_cleaned)

    return list