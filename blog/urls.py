from django.urls import path
from .views import homepage, say_hi



urlpatterns = [
    path('home/', homepage, name='homepage'),
    path('say-hi/<str:name>/', say_hi, name='say-hi'),
]