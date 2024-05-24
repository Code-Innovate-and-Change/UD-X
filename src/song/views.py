from rest_framework import generics
from .models import Lyric
from .serializers import LyricSerializer

class LyricList(generics.ListCreateAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer



































# def hello_world(request):
#     # return HttpResponse("<h1>Hello world</h1>")
#     return JsonResponse({"lyrics": [
#         {"lyric": 1,
#          "text": "I Give myself away",
#          "timestamp": "00:00:01"},
#          {"lyric": 2,
#          "text": "Oooo",
#          "timestamp": "00:00:03"},
#     ]})