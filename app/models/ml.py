from pathlib import Path
import joblib
import numpy as np
MODEL_PATH = Path(__file__).with_suffix(".joblib")

_model = None
def _load():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_from_dict(payload: dict[str, float]) -> float:
    pipe = _load()
    # Asegura que las columnas vayan en el orden que el Pipeline vio
    cols = pipe.feature_names_in_
    X = np.array([[payload[c] for c in cols]])
    return float(pipe.predict(X)[0])
