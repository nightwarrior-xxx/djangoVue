from django.contrib import admin
from django.urls import path

from catalog.views import (
    public,
    private,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/public/',public, name="apiPublic"),
    path('api/private/',private, name="apiPrivate"),
]
