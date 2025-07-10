# ERP ↔ PivotConnect Bridge

A minimal Python/FastAPI project that exposes health readings & ML predictions to an ERP and forwards
payment files to a bank‑like SFTP server, fulfilling the requirements described.

## Quick start (Docker Compose)

```bash
git clone <repo>
cd erp_bank_bridge
# Generate demo key + model
docker run --rm -v $PWD:/code -w /code python:3.12        bash -c "pip install puttykeys scikit-learn joblib cryptography && python scripts/bootstrap.py"

docker compose up --build
```

* API available at <http://localhost:8000/docs>
* SFTP server exposed on `localhost:2222`.

## Endpoints

| Method | Path | Description |
| ------ | ---- | ----------- |
| `POST` | `/auth/token` | Get JWT access token |
| `GET`  | `/readings`   | Dummy health readings |
| `POST` | `/predictions`| Predict with dummy ML |
| `POST` | `/bank/transfer` | Upload file to bank |

## Local dev

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/bootstrap.py         # create model + key
uvicorn app.main:app --reload
```
