import numpy as np

# 1. definir conjunto de ejemplo X y etiquetas y (OR)
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([0,1,1,1])

# 2. definir las épocas y tasa de aprendizaje
epochs = 10
lr = 0.1

# 3. agregar el sesgo
Xb = np.hstack([X, np.ones((X.shape[0], 1))])

# 4. inicializar los pesos
np.random.seed(42)
w = np.random.uniform(-0.5, 0.5, size=(Xb.shape[1],))

# 5. función de activación escalón
def step(z):
    return 1 if z >= 0 else 0

# 6. entrenamiento del perceptrón
for epoch in range(epochs):
    errors = 0
    for xi, yi in zip(Xb, y):
        z = np.dot(xi, w)
        yout = step(z)
        delta = yi - yout
        
        if delta != 0:
            w += lr * delta * xi
            errors += 1
    
    print(f"Epoch {epoch+1}/{epochs}, Errores: {errors}")

# 7. función de predicción
def predict(x):
    xb = np.append(x, 1)
    z = np.dot(xb, w)
    return step(z)

# 8. probar predicciones
for x in X:
    print(f"Entrada: {x}, Predicción: {predict(x)}")