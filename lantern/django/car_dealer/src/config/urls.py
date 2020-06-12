from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from apps.newsletters.views import NewsLetterView
from common.views import LoginView, logout_view, home_page

urlpatterns = [
    path("", home_page, name="homepage", ),
    path("admin/", admin.site.urls),
    path(
        "success/",
        TemplateView.as_view(template_name="index.html", ),
        name="success",
    ),
    path("newsletter/", NewsLetterView.as_view(), name="newsletter", ),
    path("login/", LoginView.as_view(), name="login", ),
    path("logout/", logout_view, name="logout", ),
    path("cars/", include("apps.cars.urls", namespace="cars_v1", )),
    path("dealers/", include("apps.dealers.urls", namespace="dealers_v1", )),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
