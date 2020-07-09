from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.newsletters.views import NewsLetterView
from common.views import LoginView, logout_view, home_page

schema_view = get_schema_view(
    openapi.Info(
        title="Car Dealer DOCS",
        default_version="v1",
        description="""All endpoints in Car Dealer DOCS are described here.
        The `swagger-ui` view can be found [here](/docs/).
        The `ReDoc` view can be found [here](/redocs/).""",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", home_page, name="homepage",),
    path("admin/", admin.site.urls),
    path(
        "success/", TemplateView.as_view(template_name="index.html",), name="success",
    ),
    path("newsletter/", NewsLetterView.as_view(), name="newsletter",),
    path("login/", LoginView.as_view(), name="login",),
    path("logout/", logout_view, name="logout",),
    path("cars/", include("apps.cars.urls", namespace="cars_v1",)),
    path("dealers/", include("apps.dealers.urls", namespace="dealers_v1",)),
    path("photos/", include("apps.photos.urls", namespace="photos_v1",)),
    path("orders/", include("apps.orders.urls", namespace="orders_v1",)),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="docs_api_v1_view",
    ),
    # path(
    #     "redocs/",
    #     schema_view.with_ui("redoc", cache_timeout=0),
    #     name="redocs_api_v1_view",
    # ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
