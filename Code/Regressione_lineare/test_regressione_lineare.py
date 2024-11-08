from regressione_lineare import RegressioneLineare
import numpy as np

# Dati di esempio: X = ore di studio, y = punteggio ottenuto
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 1.3, 3.75, 2.25])

modello = RegressioneLineare()
modello.fit(X, y)

print(f"Intercetta: {modello.intercept_}")
print(f"Coefficiente: {modello.coef_}")

# Test della predizione
X_test = np.array([[6]])
print(f"Predizione per 6 ore di studio: {modello.predict(X_test)}")
