from django.urls import path

from apps.dealers.views import DealerListView, DealerDetailView

app_name = "dealers"

urlpatterns = [
    path("", DealerListView.as_view(template_name="dealer_list.html", ), name="dealers", ),
    path("<int:id>/", DealerDetailView.as_view(template_name="dealer_detail.html", ), name="dealer_detail", ),
]
