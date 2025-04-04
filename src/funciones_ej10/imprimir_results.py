import pandas as pd

def imprimir_results (tabla_jugadores):
    df= pd.DataFrame.from_dict (tabla_jugadores, orient='index')
    df_ordenado= df.sort_values (by='points', ascending=False)
    print (df_ordenado[['kills','assists','deaths','points','MVP']])