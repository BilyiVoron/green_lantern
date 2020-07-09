from django.views.generic import ListView, DetailView

from apps.cars.models import Car


class CarListView(ListView):
    model = Car
    template_name = "car_list.html"
    paginate_by = 100


class DealerCarListView(ListView):
    model = Car
    template_name = "cars_of_dealer.html"
    pk_url_kwarg = "dealer_id"

    def get_queryset(self):
        return Car.objects.filter(dealer_id=self.kwargs.get("dealer_id", None))

    # def get_queryset(self):
    #     queryset = Car.objects.all()
    #     dealer = self.request.GET.get("dealer_id")
    #     if dealer is not None:
    #         return queryset.filter(dealer_id=dealer)
    #     else:
    #         return queryset


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"
    template_name = "car_detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
