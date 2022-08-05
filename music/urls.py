from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from music.serializers import MusicSerializers

music_router = SimpleRouter()
news_router = SimpleRouter()

music_router.register(r'music', views.MusicViewSet, basename='music_upload')
news_router.register(r'news', views.NewsViewSet, basename='news_upload')

urlpatterns = [
    # path('', views.upload_music),
    path('api/', include(music_router.urls)),
    path('api/', include(news_router.urls)),

]
