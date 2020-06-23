from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.cars.models import Color, CarModel, CarBrand, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    pass


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "_image")

    def _image(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="height: 50px">')
        return "----"
