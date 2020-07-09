from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.photos.views import UploadImageView

app_name = "photos"

urlpatterns = [
    path(
        "upload_image/", login_required(UploadImageView.as_view()), name="upload_image"
    ),
]
