import calc_points, actualizar_tabla


def simulacion_partidas (rounds):
    tabla_jugadores = {}
    for nro_round, round in enumerate (rounds, start=1):
        result_round={}

        for jugador, stats in round.items():
            kills = stats ['kills']
            assists = stats ['assists']
            deaths= stats ['deaths']
            points=calc_points (kills, assists, deaths)
            result_round[jugador] = points
            actualizar_tabla (jugador, kills, assists, deaths, points, tabla_jugadores)
    
