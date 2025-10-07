def combinaciones_suma(candidatos, T):
    resultado = []

    def backtrack(inicio, objetivo, combinacion_actual):
        # Si el objetivo llega a 0, se encontró una combinación válida
        if objetivo == 0:
            resultado.append(list(combinacion_actual))
            return
        # Si el objetivo es negativo, no hay solución en este camino
        if objetivo < 0:
            return

        # Se recorre desde el inicio
        for i in range(inicio, len(candidatos)):
            num = candidatos[i]
            combinacion_actual.append(num)
            # Se establece la reutilizacion de numeros
            backtrack(i, objetivo - num, combinacion_actual)
            combinacion_actual.pop()

    backtrack(0, T, [])
    return resultado


# Ejemplo 1
print(combinaciones_suma([2, 3, 6, 7], 7))

# Ejemplo 2
print(combinaciones_suma([2, 3, 5], 8))
