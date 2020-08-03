from django.urls import path

from apps.cars.views import CarListView, CarDetailView, DealerCarListView

app_name = "cars"

urlpatterns = [
    path("", CarListView.as_view(), name="cars", ),
    path("dealer/<int:dealer_id>/cars_of_dealer/", DealerCarListView.as_view(), name="cars_of_dealer", ),
    path("<int:id>/", CarDetailView.as_view(), name="car_detail", ),
]
