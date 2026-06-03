import numpy as np

# 1. Datos (AND)
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([0, 1, 1, 1])

# 2. Parámetros
epochs = 1000
lr = 0.1

# 3. Agregar sesgo
Xb = np.hstack([X, np.ones((X.shape[0], 1))])

# 4. Inicializar pesos
np.random.seed(42)
w = np.random.uniform(-0.5, 0.5, size=(Xb.shape[1],))

# 5. Entrenamiento (MODELO LINEAL)
for epoch in range(epochs):
    error_total = 0
    
    for xi, yi in zip(Xb, y):
        z = np.dot(xi, w)   # salida lineal
        
        delta = yi - z      # error
        
        # Actualización de pesos
        w += lr * delta * xi
        
        error_total += abs(delta)
    
    print(f"Epoch {epoch+1}, Error total: {error_total:.4f}")
    
    # condición de parada
    if error_total < 0.01:
        print(f"\nConvergencia alcanzada en la época {epoch+1}")
        break

# 6. Mostrar pesos finales
print("\nPesos finales:", w)
print(f"Ecuación: {w[0]:.4f}*x1 + {w[1]:.4f}*x2 + {w[2]:.4f} = 0")

# 7. Función de predicción
def predict(x):
    xb = np.append(x, 1)   # agregar sesgo
    z = np.dot(xb, w)
    
    # Convertir a clase
    return 1 if z >= 0 else -1

# 8. Probar con los datos
print("\nPredicciones:")
for x in X:
    print(f"Entrada: {x}, Predicción: {predict(x)}")