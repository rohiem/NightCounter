# Use Python 3.8.5 on Alpine Linux
FROM python:3.8.5-alpine

# Set environment variables to prevent Python from writing .pyc files
# and to ensure stdout and stderr are unbuffered (helpful for Docker logs)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary build dependencies and basic tools
RUN apk update && apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    linux-headers \
    libffi-dev \
    openssl-dev \
    make \
    && apk add --no-cache \
    libpq \
    postgresql-dev \
    curl \
    bash \
    && pip install --upgrade pip setuptools wheel \
    && rm -rf /var/cache/apk/*

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
# Make sure you have a requirements.txt file with your project dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run your application (customize as needed)
#CMD ["python", "your_app.py"]  # Change 'your_app.py' to your main script or entry point


# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Run Gunicorn to serve Django
CMD ["gunicorn", "wordcount.wsgi:application", "--bind", "0.0.0.0:8000"]

#CMD ["celery", "-A", "wordcount", "worker", "--loglevel=info"]