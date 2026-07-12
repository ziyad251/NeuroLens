FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python deps
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend /app/backend

# Copy models (a trained model is required for prediction requests)
COPY models /app/models

# Default env values (override via docker-compose)
ENV FLASK_PORT=5000
ENV FLASK_DEBUG=0
ENV MODEL_PATH=/app/models/model.pth
ENV MONGODB_URI=mongodb://mongo:27017
ENV MONGODB_DB=alzheimers
ENV CORS_ORIGINS=http://localhost:8501

EXPOSE 5000

CMD ["python", "-m", "backend.app"]
