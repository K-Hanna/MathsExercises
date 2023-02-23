from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('maths/', include('maths.urls')),
    path('admin/', admin.site.urls),
]