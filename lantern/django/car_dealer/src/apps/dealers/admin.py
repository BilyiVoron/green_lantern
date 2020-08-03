from django.contrib import admin

from apps.dealers.models import Dealer, Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    pass
