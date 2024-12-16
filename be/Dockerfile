# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Add build arguments
ARG SECRET_KEY
ARG DEBUG
ARG DOMAIN
ARG EXEC_ENV
ARG DB_NAME
ARG DB_USER
ARG DB_PWD
ARG DB_HOST
ARG DB_PORT
ARG USE_S3
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_STORAGE_BUCKET_NAME
ARG AWS_S3_REGION_NAME

# Set environment variables from build arguments
ENV SECRET_KEY=$SECRET_KEY
ENV DEBUG=$DEBUG
ENV DOMAIN=$DOMAIN
ENV EXEC_ENV=$EXEC_ENV
ENV DB_NAME=$DB_NAME
ENV DB_USER=$DB_USER
ENV DB_PWD=$DB_PWD
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV USE_S3=$USE_S3
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME
ENV AWS_S3_REGION_NAME=$AWS_S3_REGION_NAME

# Install system dependencies including PostGIS requirements
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR .

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run gunicorn
CMD ["gunicorn", "proj.wsgi:application", "--bind", "0.0.0.0:8000"]
