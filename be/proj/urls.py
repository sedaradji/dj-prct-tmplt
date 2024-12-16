"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import logging

import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import HttpResponse, render
from django.urls import path

logger = logging.getLogger(__name__)


def serve_index(request):
    """Serve the index.html file from S3 or local."""
    if not settings.USE_S3:
        return render(request, "index.html")

    # S3 handling for production
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,  # Add this if you have region configured
        )
        response = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key="index.html")
        content = response["Body"].read().decode("utf-8")

        # now we need to edit the template to include the correct static files
        # The static urls are relative urls, we need to replace them with the correct ones
        content = content.replace(
            "/static/", settings.STATIC_URL
        )  # Replace with the correct static URL
        content = content.replace(
            "/media/", settings.MEDIA_URL
        )  # Replace with the correct media URL

        return HttpResponse(content, content_type="text/html")
    except ClientError as e:
        logger.error(f"Error loading template: {str(e)}")
        return HttpResponse("", status=500)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", serve_index, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
