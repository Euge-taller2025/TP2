#funcion ejercicio 8

def anagramas (word1,word2):
    split1= list(word1)
    split2= list(word2)
    if len(split1) != len(split2): 
        return False
    else:
        for i in split1:
            if i not in split2:
                return False
        return True
