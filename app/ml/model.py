from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import numpy as np


# ----- Schémas d'entrée/sortie pour FastAPI -----

class SimpleFeatures(BaseModel):
    feature_1: float
    feature_2: float


class SimplePrediction(BaseModel):
    prediction: float


# ----- Mini modèle en mémoire (exemple) -----

# On entraîne juste un modèle jouet ici pour que l'endpoint fonctionne.
# Plus tard, tu chargeras un vrai modèle entraîné depuis un .pkl.
X_train = np.array([[0, 0], [1, 1], [2, 3], [4, 5]], dtype=float)
y_train = np.array([0, 1, 3, 5], dtype=float)

_model = LinearRegression()
_model.fit(X_train, y_train)


def predict_simple(features: SimpleFeatures) -> SimplePrediction:
    x = np.array([[features.feature_1, features.feature_2]], dtype=float)
    y_pred = float(_model.predict(x)[0])
    return SimplePrediction(prediction=y_pred)
