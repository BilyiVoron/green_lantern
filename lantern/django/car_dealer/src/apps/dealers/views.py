from django.views.generic import DetailView, ListView

from apps.dealers.models import Dealer


class DealerListView(ListView):
    model = Dealer
    template_name = "dealer_list.html"


class DealerDetailView(DetailView):
    model = Dealer
    context_object_name = "dealer"
    template_name = "dealer_detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
