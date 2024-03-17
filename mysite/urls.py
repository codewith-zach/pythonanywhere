from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to mysite!")


urlpatterns = [
    path('', index),  # Direct root URL to the index view
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
