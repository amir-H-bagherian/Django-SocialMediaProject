from django.urls import path
from .views import homepage, say_hi, get_post, get_all_posts, delete_post



urlpatterns = [
    path('home/', homepage, name='homepage'),
    path('say-hi/<str:name>/', say_hi, name='say-hi'),
    path('get/<int:id>/', get_post, name='get-post'),
    path('get/', get_all_posts, name='get-all-posts'),
    path('delete/<int:id>/', delete_post, name='delete-post'),
]