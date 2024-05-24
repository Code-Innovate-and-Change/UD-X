from rest_framework import serializers 

from .models import Lyric, LyricLine


class LyricLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LyricLine
        fields = "__all__"


class LyricSerializer(serializers.ModelSerializer):
    lines = serializers.SerializerMethodField()

    class Meta:
        model = Lyric 
        fields = ("date_added", "lines",)

    def get_lines(self, lyric_instance):
        return LyricLineSerializer(lyric_instance.lyricline_set.all(), many=True).data