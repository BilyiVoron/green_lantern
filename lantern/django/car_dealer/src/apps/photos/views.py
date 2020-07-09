from django.urls import reverse
from django.views.generic import FormView

from apps.photos.forms import ImageForm
from apps.photos.models import Photo


class UploadImageView(FormView):
    model = Photo
    form_class = ImageForm
    template_name = "image_uploading.html"
    # pk_url_kwarg = "dealer_id"

    def get_success_url(self):
        return reverse("success")

    def form_valid(self, form):
        form.instance.dealer = self.request.user
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(UploadImageView, self).get_form_kwargs()
        kwargs["dealer_id"] = self.request.user.pk
        return kwargs
