from django.db import router
from posts.views import my_view
from rest_framework import routers
from django.urls.conf import include
from django.urls import path
from tweets.views import TrendsviewSet, TweetViewSet,LikeViewSet,RetweetviewSet, index


router = routers.DefaultRouter()
router.register(r'', TweetViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'Retweet',RetweetviewSet)
router.register(r'Trends',TrendsviewSet)


urlpatterns = [
    path('index/', index),
    path("", include(router.urls))
]
