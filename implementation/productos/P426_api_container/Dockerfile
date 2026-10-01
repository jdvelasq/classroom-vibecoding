FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir --requirement requirements.txt

COPY implementation/productos/P426_api_container/src src

CMD ["flask", "--app", "src.main", "run", "--host", "0.0.0.0", "--port", "8000"]
