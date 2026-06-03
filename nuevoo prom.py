import random

# Población inicial con 20 números recolectados del 1 al 10
poblacion = [1, 5, 3, 8, 2, 7, 10, 4, 6, 9,
             2, 8, 1, 7, 5, 3, 10, 6, 4, 9]

print("Generacion 0:", poblacion)

# Selección de padres
padres = poblacion[:3]
print("Padres seleccionados:", padres)

hijos = []

# Crear hijos
for i in range(0, len(padres) - 1):
    for j in range(i + 1, len(padres)):

        padre1 = padres[i]
        padre2 = padres[j]

        # Operaciones matemáticas
        hijo1 = padre1 + padre2
        hijo2 = padre1 * padre2

        # Potencia limitada
        if padre2 < 6:
            hijo3 = padre1 ** padre2
        else:
            hijo3 = padre1

        hijos.append(hijo1)
        hijos.append(hijo2)
        hijos.append(hijo3)

# Mutación
mutado = random.randint(0, len(hijos) - 1)

# Invertir el número seleccionado
hijos[mutado] = int(str(hijos[mutado])[::-1])

print("Generacion 1 - hijos despues de la mutacion:", hijos)

individuos = hijos
maximo = max(individuos)

print("Numero natural mas grande encontrado:", maximo)

generacion = 1

# Ciclo de generaciones
while maximo <= 10**100:

    padres = individuos[:3]
    hijos = []

    for i in range(0, len(padres) - 1):
        for j in range(i + 1, len(padres)):

            padre1 = padres[i]
            padre2 = padres[j]

            hijo1 = padre1 + padre2
            hijo2 = padre1 * padre2

            if padre2 < 6:
                hijo3 = padre1 ** padre2
            else:
                hijo3 = padre1

            hijos.append(hijo1)
            hijos.append(hijo2)
            hijos.append(hijo3)

    print("Hijos generados:", hijos)

    # Nueva mutación
    mutado = random.randint(0, len(hijos) - 1)
    hijos[mutado] = int(str(hijos[mutado])[::-1])

    print(f"Generacion {generacion} - hijos despues de la mutacion:", hijos)

    individuos = hijos
    maximo = max(individuos)

    print("Maximo actual:", maximo)

    generacion += 1

    # Seguridad para evitar ciclo infinito
    if generacion > 20:
        print("Limite de generaciones alcanzado")
        break