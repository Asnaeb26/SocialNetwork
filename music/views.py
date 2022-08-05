from .models import *
from . import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class MusicViewSet(ModelViewSet):
    """Список всех треков"""
    queryset = Music.objects.all()
    serializer_class = serializers.MusicSerializers
    # lookup_field = 'id'


class NewsViewSet(ModelViewSet):
    """Список всех новостей"""
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializers
