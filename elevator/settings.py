"""
Django settings for elevator project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-x1jo&n$*i-zor1awf_3+z15xkoa+e)52t@v1=e9sk_omrr$mi5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "elevator_app",
    "rest_framework",
    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "elevator.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "elevator.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REDIS_HOST = 'localhost'
REDIS_PORT = 6379


REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS":"drf_spectacular.openapi.AutoSchema"
}

SPECTACULAR_SETTINGS = {
    "TITLE":"ELEVATOR SYSTEM",
}

# Sure, here are the more detailed step-by-step instructions for connecting your Python/Django backend and React frontend on Google Cloud Platform (GCP):

# Deploy Django on GCP:
# Create a new GCP project if you haven't already.
# Set up a virtual environment and install dependencies for your Django project.
# Choose a hosting service, such as App Engine or Compute Engine, and deploy your Django application to GCP.
# If using App Engine, create an app.yaml file to specify the runtime environment and other settings for your app.
# Expose Django backend APIs as RESTful APIs:
# Install and configure Django REST Framework for your Django project.
# Define your API endpoints and configure serializers for your models.
# Test your API endpoints using tools like Postman or cURL.
# Use Google Cloud Pub/Sub for message queue:
# Create a topic in Pub/Sub for your backend API.
# Use the google-cloud-pubsub Python client library to publish messages to the topic.
# In your Django application, set up a Pub/Sub subscriber to receive and process incoming messages.
# Send HTTP requests from React frontend to Django backend:
# In your React project, use the fetch API or a library like Axios to make HTTP requests to your Django backend API endpoints.
# Use JSON as the data format for your request and response payloads.
# Handle errors and HTTP status codes appropriately in your frontend code.
# Use Google Cloud Storage API for file storage:
# Create a Cloud Storage bucket to store files uploaded by your frontend.
# Use the google-cloud-storage Python client library to upload and download files to/from the bucket.
# In your Django application, define views for handling file uploads and downloads.////
# Set up authentication and authorization:
# Use Google Cloud Identity and Access Management (IAM) to manage authentication and authorization for your application.
# Configure your API endpoints to require authentication and enforce appropriate access controls.
# Use Google Cloud Load Balancing for scalability: ///////
# Create a load balancer to distribute incoming traffic to your backend services.////
# Configure your backend services to scale up and down dynamically based on traffic patterns.////
# By following these steps, you should be able to connect your Python/Django backend and React frontend on GCP with ease.





# If you plan on deploying your website frequently, then you may want to consider using a Continuous Integration/Continuous Deployment (CI/CD) pipeline to automate the deployment process.

# Here are the steps to set up a CI/CD pipeline for your Python/Django backend and React frontend on GCP:

# Set up a source code repository:
# Create a repository on a platform like GitHub or Bitbucket to store your code.
# Push your Django backend and React frontend code to the repository.
# Set up a CI/CD pipeline using Cloud Build:
# Create a Cloud Build trigger that listens for changes to your repository.
# Specify the build steps in a cloudbuild.yaml file that includes the following steps:
# Install dependencies for your backend and frontend code.
# Run tests for your backend and frontend code.
# Build and bundle your React frontend code.
# Deploy your backend and frontend code to GCP using the appropriate deployment method (e.g., App Engine, Compute Engine, Cloud Storage).
# Configure Cloud Build to deploy your code to a staging environment first for testing before deploying to production.
# Monitor and troubleshoot the CI/CD pipeline:
# Use Stackdriver Logging to monitor the CI/CD pipeline and troubleshoot any issues that arise.
# Use Stackdriver Trace to analyze the performance of your application and identify any bottlenecks.
# By setting up a CI/CD pipeline, you can automate the deployment process and make it easier to deploy your website frequently.