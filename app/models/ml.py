from pathlib import Path
import numpy as np
import joblib

MODEL_PATH = Path(__file__).with_suffix(".joblib")

def _train_dummy():
    from sklearn.linear_model import LogisticRegression
    X, y = np.random.rand(200, 3), np.random.randint(0, 2, 200)
    model = LogisticRegression().fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

def _load():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    return _train_dummy()

_model = None

def predict(features: list[float]) -> float:
    global _model
    if _model is None:
        _model = _load()
    import numpy as np
    return float(_model.predict(np.array(features).reshape(1, -1))[0])
