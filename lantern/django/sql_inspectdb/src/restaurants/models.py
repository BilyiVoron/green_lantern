# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "country"


class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "city"


class Season(models.Model):
    season_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "season"


class Dish(models.Model):
    dish_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    ingredients = models.CharField(max_length=255, blank=True, null=True)
    recipe = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField()
    price = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "dish"


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    dish = models.ForeignKey(Dish, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "menu"


class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(unique=True, max_length=100)
    menu = models.ForeignKey(Menu, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "restaurant"


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    position = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100)
    country = models.ForeignKey(Country, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True)
    phone_no = models.IntegerField()
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "employee"
