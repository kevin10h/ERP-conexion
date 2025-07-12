from pathlib import Path
import joblib
import numpy as np
from joblib import load
pipe = load("app/models/ml.joblib")

MODEL_PATH = Path(__file__).with_suffix(".joblib")

_model = None
def _load():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_from_dict(payload: dict[str, float]) -> float:
    pipe = _load()

    # Detecta scikit-learn vs CatBoost
    if hasattr(pipe, "feature_names_in_"):        # scikit-learn
        cols = list(pipe.feature_names_in_)
    elif hasattr(pipe, "feature_names_"):         # CatBoost
        cols = list(pipe.feature_names_)
    else:                                         # último recurso
        cols = list(payload.keys())

    X = np.array([[payload[c] for c in cols]], dtype=float)
    return float(pipe.predict(X)[0])

# Scikit-learn usa feature_names_in_, CatBoost usa feature_names_
names = getattr(pipe, "feature_names_in_", None) or getattr(pipe, "feature_names_")
print(list(names))



