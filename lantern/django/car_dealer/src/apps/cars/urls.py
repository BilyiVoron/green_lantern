from django.urls import path

from apps.cars.views import CarListView, CarDetailView, DealerCarListView

app_name = "cars"

urlpatterns = [
    path("", CarListView.as_view(template_name="car_list.html", ), name="cars", ),
    path(
        "cars_of_dealer/",
        DealerCarListView.as_view(template_name="cars_of_dealer.html", ),
        name="cars_of_dealer",
    ),
    path(
        "<int:id>/",
        CarDetailView.as_view(template_name="car_detail.html", ),
        name="car_detail",
    ),
]
