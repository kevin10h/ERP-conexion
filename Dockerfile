# Dockerfile
FROM python:3.12-slim
WORKDIR /code

# ——— dependencias del sistema (ssh-keygen + puttygen) ———
RUN apt-get update \
 && apt-get install -y --no-install-recommends openssh-client putty-tools \
 && rm -rf /var/lib/apt/lists/*
# ————————————————————————————————————————————————

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
