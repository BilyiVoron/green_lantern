from django.views.generic import ListView, DetailView

from apps.cars.models import Car


class CarListView(ListView):
    model = Car
    template_name = "car_list.html"


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"
    template_name = "car_detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
