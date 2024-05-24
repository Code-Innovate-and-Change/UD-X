from django.urls import path
from .views import LyricList


urlpatterns = [
    path("lyrics", LyricList.as_view(), name="lyrics_list")
]