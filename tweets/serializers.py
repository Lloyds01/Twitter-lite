from django.db.models import fields
from rest_framework.fields import Field
from rest_framework.serializers import ModelSerializer
from .models import Retweet, Trends, Tweet, Like

class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields ="__all__"

class LikeSerializer(ModelSerializer):
    class Metta:
        model = Like
        fields = "__all__"

class Retweetserializer(ModelSerializer):
    class Metta:
        model = Retweet
        fields = "__all__"

class Trendsserializer(ModelSerializer):
    class Metta:
        model = Trends
        fields = "__all__"