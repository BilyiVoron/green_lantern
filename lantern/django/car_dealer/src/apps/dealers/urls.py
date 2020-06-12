from django.urls import path

from apps.dealers.views import DealerListView, DealerDetailView

app_name = "dealers"

urlpatterns = [
    path("", DealerListView.as_view(), name="dealers", ),
    path("<int:id>/", DealerDetailView.as_view(), name="dealer_detail", ),
]
