from calc_points import calc_points 
from actualizar_tabla import actualizar_tabla
from calc_mvp import calc_MVP
from imprimir_results import imprimir_results


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

        MVP = calc_mvp (result_round)
        tabla_jugadores [MVP]['MVP'] +=1

    imprimir_results(tabla_jugadores)