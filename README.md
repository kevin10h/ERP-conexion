![CI](https://github.com/kevin10h/ERP-conexion/actions/workflows/ci.yml/badge.svg)

# Puente ERP ↔ PivotConnect

Proyecto mínimo en **Python/FastAPI** que expone lecturas de salud y predicciones ML a un ERP, y reenvía
archivos de pago a un servidor SFTP tipo banco.

## Inicio rápido (Docker Compose)

```bash
git clone <repo>
cd erp_bank_bridge
# Generar clave demo + modelo
docker run --rm -v $PWD:/code -w /code python:3.12 \
  bash -c "pip install puttykeys scikit-learn joblib cryptography && \
           python scripts/bootstrap.py"

docker compose up --build
```

* **API** disponible en [`http://localhost:8000/docs`](http://localhost:8000/docs)
* **DEMO** disponible en [`http://localhost:8000/demo/live_demo.html`](http://localhost:8000/demo/live_demo.html)
* **Servidor SFTP** expuesto en [`sftp://localhost:2222`](sftp://localhost:2222)

```
```
## Endpoints

| Método | 	Ruta | Descripción |
| ------ | ---- | ----------- |
| `POST` | `/auth/token` | 	Obtener token JWT |
| `GET`  | `/readings`   | Lecturas de salud de ejemplo |
| `POST` | `/predictions`| Predicción Modelo de Machine learning |
| `POST` | `/bank/transfer` | Subir archivo al banco (SFTP) |
```
```
## Desarrollo local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/bootstrap.py         # create model + key
uvicorn app.main:app --reload
```

