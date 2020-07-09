from django import forms

from apps.photos.models import Photo


class ImageForm(forms.Form):
    image = forms.ImageField()

    class Meta:
        model = Photo
        fields = ["image", "car"]
