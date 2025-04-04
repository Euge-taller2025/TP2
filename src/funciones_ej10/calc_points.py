def calc_points (kills, assists, deaths):
    return (kills *3) + (assists *1) + (-1 if deaths==True else 0)
