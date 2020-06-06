from django.db import models


class OrderQuerySet(models.QuerySet):
    def reserved(self):
        return self.filter(status="reserved")

    def paid(self):
        return self.filter(status="paid")

    def waiting_for_payment(self):
        return self.filter(status="waiting for payment")

    def archived(self):
        return self.filter(status="archived")


class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("car",)
