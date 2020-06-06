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
