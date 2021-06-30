from django.urls import path, include
from posts.views import my_view


urlpatterns = [
    path('Loans/', my_view),
]
