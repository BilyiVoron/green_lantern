from django.urls import path

from apps.cars.views import CarListView, CarDetailView

app_name = "cars"

urlpatterns = [
    path("", CarListView.as_view(template_name="car_list.html", ), name="cars", ),
    path("<int:id>/", CarDetailView.as_view(template_name="car_detail.html", ), name="car_detail", ),
]
