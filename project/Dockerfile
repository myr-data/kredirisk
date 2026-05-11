FROM python:3.10-slim

# working directory inside container
WORKDIR /app

# system dependencies (safe default for ML libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copy only project folder contents
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose FastAPI port
EXPOSE 8000

# run API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]