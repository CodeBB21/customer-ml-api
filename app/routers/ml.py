from fastapi import APIRouter
from ..ml.model import SimpleFeatures, SimplePrediction, predict_simple

router = APIRouter(prefix="/ml", tags=["ml"])


@router.post("/predict", response_model=SimplePrediction)
def predict(features: SimpleFeatures):
    """
    Endpoint de démonstration.
    Plus tard : remplacer par ton vrai modèle (churn, scoring client, etc.).
    """
    return predict_simple(features)
