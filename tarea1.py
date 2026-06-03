import random

poblacion = [8, 4, 7, 1, 7, 6]
print("generacion 0", poblacion)

padres = poblacion[:3]
print("padres seleccionados", padres)

hijos = []

for i in range(0, len(padres)-1):
    for j in range(i+1, len(padres)):
        padre1 = padres[i]
        padre2 = padres[j]

        hijo1 = padre1 + padre2
        hijo2 = padre1 * padre2
        
        # NUEVA OPERACIÓN: potencia (limitada para evitar números gigantes)
        hijo3 = padre1 ** padre2 if padre2 < 6 else padre1

        hijos.append(hijo1)
        hijos.append(hijo2)
        hijos.append(hijo3)

mutado = random.randint(0, len(hijos)-1)
hijos[mutado] = int(str(hijos[mutado])[::-1])

print("generacion1-hijos despues de la mutacion", hijos)

individuos = hijos
maximo = max(individuos)
print("numero natural mas grande encontrado", maximo)

generacion = 1

while maximo <= 10**100:  # objetivo: llegar a 10^100
    padres = individuos[:3]
    hijos = []

    for i in range(0, len(padres)-1):
        for j in range(i+1, len(padres)):
            padre1 = padres[i]
            padre2 = padres[j]

            hijo1 = padre1 + padre2
            hijo2 = padre1 * padre2
            hijo3 = padre1 ** padre2 if padre2 < 6 else padre1

            hijos.append(hijo1)
            hijos.append(hijo2)
            hijos.append(hijo3)

    print("hijos generados", hijos)

    mutado = random.randint(0, len(hijos)-1)
    hijos[mutado] = int(str(hijos[mutado])[::-1])

    print(f"generacion {generacion} - hijos despues de la mutacion", hijos)

    individuos = hijos
    maximo = max(individuos)

    print(f"maximo actual: {maximo}")

    generacion += 1

    # seguridad para que no sea infinito
    if generacion > 20:
        break