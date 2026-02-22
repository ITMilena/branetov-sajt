from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),

    # Tvoje stranice (app gradnja)
    path("", include("gradnja.urls")),

    # Auto browser reload (DEV only)
    path("__reload__/", include("django_browser_reload.urls")),
]
