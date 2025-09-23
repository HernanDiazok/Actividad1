def calcular_puntos(equipo):
    # calcula el puntaje total de un equipo basado en innovación, presentación y errores
    # +3 puntos por innovación - +1 por presentación - -1 por errores
    return equipo['innovacion'] * 3 + equipo['presentacion'] * 1 - (1 if equipo['errores'] else 0)

def determinar_mer(ronda):
    # Devuelve el equipo con mayor puntaje en la ronda.
    puntajes = list(map(lambda item: (item[0], calcular_puntos(item[1])), ronda.items()))
    return max(puntajes, key=lambda x: x[1])[0]  


def mostrar_ranking(equipos):
    # Imprime el ranking ordenado por puntos totales de cada equipo de forma descendente.
    ranking_ordenado = sorted(equipos.items(), key=lambda item: item[1]['puntos'], reverse=True)

    print("\n🏅 Ranking:")
    print(f"{'|Equipo|':<10} {'|Innovacion|':<12} {'|Presentacion|':<14} {'|Errores|':<8} {'|MER|':<9} {'|Puntos|':<10}")
    print("-" * 75)

    for nombre, datos in ranking_ordenado:
        print(f"{nombre:<10} {datos['innovacion']:<12} {datos['presentacion']:<14} {datos['errores']:<8} {datos['mer']:<9} {datos['puntos']:<10}")
