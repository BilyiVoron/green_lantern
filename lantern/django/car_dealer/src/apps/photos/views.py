from django.urls import reverse
from django.views.generic import FormView

from apps.photos.forms import ImageForm
from apps.photos.models import Photo


class UploadImageView(FormView):
    model = Photo
    form_class = ImageForm
    template_name = "image_uploading.html"

    def get_success_url(self):
        return reverse("cars_v1:cars")

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
