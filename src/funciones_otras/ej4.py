#funcion ejercicio 4

def validacion (user):
    if len(user)<5: 
        return False
    if not user.isalnum():
        return False
    if not any(u.islower() for u in user):
        return False
    if not any(u.isupper() for u in user):
        return False
    if not any (u.isdigit() for u in user):
        return False
    return True