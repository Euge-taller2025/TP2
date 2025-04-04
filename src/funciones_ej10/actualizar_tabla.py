def actualizar_tabla(jugador, kills, assists, deaths, points, tabla_jugadores):
    if jugador not in tabla_jugadores:
        tabla_jugadores[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'puntos_totales': 0}
    tabla_jugadores[jugador]['kills'] += kills
    tabla_jugadores[jugador]['assists'] += assists
    tabla_jugadores[jugador]['deaths'] += 1 if deaths==True else 0
    tabla_jugadores[jugador]['puntos_totales'] += points