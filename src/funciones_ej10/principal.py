from funciones_ej10.calc_points import calc_points 
from funciones_ej10.actualizar_tabla import actualizar_tabla
from funciones_ej10.calc_mvp import calc_mvp
from funciones_ej10.imprimir_results import imprimir_results


def simulacion_partidas (rounds):
    """variable dic donde voy a acumular los resultados de las rondas x jugador"""
    tabla_jugadores = {}

    """iteracion ronda por ronda que devuelve el nro de ronda y el contenido"""
    for nro_round, round in enumerate (rounds, start=1):
        """variable acumuladora de los puntos totales de cada jugador"""
        result_round={}

        """iteracion dentro de la ronda x donde para cada jugador se realizan los calculos necesarios"""
        for jugador, stats in round.items():

            """se procede a guardar el detalle de la ronda para ese jugador x"""
            kills = stats ['kills']
            assists = stats ['assists']
            deaths= stats ['deaths']
            """calculo de puntaje"""
            points=calc_points (kills, assists, deaths)
            result_round[jugador] = points
            """act de la tabla de resultados final"""
            actualizar_tabla (jugador, kills, assists, deaths, points, tabla_jugadores)

        """luego de procesada la ronda x para cada jugador se determina el jugador MVP"""
        MVP = calc_mvp (result_round)
        """dentro de la tabla de resultados, en una nueva columna el dic se guarda el contador de veces que el jugador fue MVP"""
        tabla_jugadores [MVP]['MVP'] +=1

        """impresion de tabla de resultados ronda x """
        print (f'Ranking ronda {nro_round}: \n')
        imprimir_results(tabla_jugadores)
        print ()

    """luego de procesada toda la partida se imprime el ranking final con el resultado acumulado de todas las rondas x jugador"""
    print ('Ranking final: \n')
    imprimir_results(tabla_jugadores)