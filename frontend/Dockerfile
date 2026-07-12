FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python deps
COPY frontend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend code
COPY frontend /app/frontend

EXPOSE 8501

# Streamlit expects the entry script at frontend/app.py
CMD ["streamlit", "run", "/app/frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
