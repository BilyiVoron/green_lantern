from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.orders.forms import OrderForm
from apps.orders.models import Order


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("success")
    template_name = "create_order.html"

    def form_valid(self, form):
        form.save()
        return super(CreateOrderView, self).form_valid(form)
