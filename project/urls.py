from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.home, name="home"),
    path('result/', app.views.result, name="result"),
]
