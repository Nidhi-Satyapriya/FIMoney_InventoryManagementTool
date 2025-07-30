# Use official Python image for backend
FROM python:3.11-slim AS backend

WORKDIR /app/backend

COPY backend/ ./
RUN pip install --no-cache-dir -r requirements.txt

# Use official Node image for frontend build
FROM node:20-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/ ./
RUN npm install && npm run build

# Final image: serve frontend with nginx, run backend with uvicorn
FROM python:3.11-slim

# Backend setup
WORKDIR /app/backend
COPY --from=backend /app/backend /app/backend
RUN pip install --no-cache-dir -r requirements.txt

# Frontend setup
WORKDIR /app/frontend
COPY --from=frontend-build /app/frontend/dist /app/frontend/dist

# Nginx for frontend
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 8000 80

# Start both backend and nginx
CMD service nginx start && uvicorn app.main:app --host 0.0.0.0 --port 8000
