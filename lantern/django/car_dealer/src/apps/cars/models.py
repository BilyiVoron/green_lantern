from datetime import date

from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _

from djmoney.models.fields import MoneyField
from apps.cars.managers import CarManager, CarQuerySet
from common.models import BaseDateAuditModel


class Color(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        indexes = [Index(fields=("name",))]

        verbose_name = _("Color")
        verbose_name_plural = _("Colors")

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(null=True, blank=False)

    class Meta:
        ordering = ("name",)
        indexes = [Index(fields=("name",))]
        verbose_name = _("Car brand")
        verbose_name_plural = _("Car brands")

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=64, unique=True)
    brand = models.ForeignKey("CarBrand", on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)
        indexes = [
            Index(fields=("name",)),
        ]
        verbose_name = _("Car model")
        verbose_name_plural = _("Car models")

    def __str__(self):
        return self.name


class Car(BaseDateAuditModel):
    STATUS_PENDING = "pending"
    STATUS_PUBLISHED = "published"
    STATUS_SOLD = "sold"
    STATUS_ARCHIVED = "archived"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    AUTOMATIC_TRANSMISSION = "automatic transmission"
    SEMI_AUTOMATIC_TRANSMISSION = "semi-automatic transmission"
    MANUAL_TRANSMISSION = "manual transmission"

    GEAR_BOX_CHOICES = (
        (AUTOMATIC_TRANSMISSION, "automatic transmission"),
        (SEMI_AUTOMATIC_TRANSMISSION, "semi-automatic transmission"),
        (MANUAL_TRANSMISSION, "manual transmission"),
    )

    WHEEL_DRIVE_CHOICE_YES = "Yes"
    WHEEL_DRIVE_CHOICE_NO = "No"

    ALL_WHEEL_DRIVE_CHOICES = (
        (WHEEL_DRIVE_CHOICE_YES, "Yes"),
        (WHEEL_DRIVE_CHOICE_NO, "No"),
    )

    objects = CarManager.from_queryset(CarQuerySet)()
    views = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=75)
    number = models.CharField(max_length=16, unique=True)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, blank=True
    )
    dealer = models.ForeignKey(
        "dealers.Dealer", on_delete=models.CASCADE, related_name="cars"
    )

    model = models.ForeignKey(
        "CarModel", on_delete=models.SET_NULL, null=True, blank=False
    )
    color = models.ForeignKey(
        "Color", on_delete=models.SET_NULL, null=True, blank=False
    )
    extra_title = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Title second part")
    )
    first_registration_date = models.DateField(
        auto_now_add=False, default=date.today, verbose_name="First registration date"
    )
    engine_type = models.CharField(max_length=25, blank=True)
    engine_power = models.IntegerField(null=True)
    fuel_type = models.CharField(max_length=25, null=True, blank=False)
    fuel_capacity = models.IntegerField(null=True)
    gear_box = models.CharField(
        max_length=27, choices=GEAR_BOX_CHOICES, null=True, blank=False
    )
    all_wheel_drive = models.CharField(
        max_length=3, choices=ALL_WHEEL_DRIVE_CHOICES, null=True, blank=False
    )
    doors = models.IntegerField(null=True)
    sitting_place = models.IntegerField(null=True)
    trunk_capacity = models.IntegerField(null=True)
    population_type = models.CharField(max_length=55, null=True, blank=False)
    price = MoneyField(
        max_digits=9, decimal_places=2, default_currency="USD", null=True
    )

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

        indexes = [Index(fields=["status", ])]

    def save(self, *args, **kwargs):
        order_number_start = 7600000
        if not self.pk:
            super().save(*args, **kwargs)
            self.number = f"LK{order_number_start + self.pk}"
            self.save()
        else:
            super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.status = self.STATUS_ARCHIVED
        self.save()

    @property
    def title(self):
        return f'{self.model.brand} {self.extra_title or ""}'  # do not show None

    def __str__(self):
        return self.title


class Property(models.Model):
    name = models.CharField(max_length=55)
    category = models.CharField(max_length=55)
    car = models.ManyToManyField("Car", related_name="properties")
