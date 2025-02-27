from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar_app/', include('calendar_app.urls')),
    path('user_app/', include('user_app.urls')),
]
