from django.urls import path
from .views import HomePageView, obtener_informacion, video, audio

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('obtener_informacion/', obtener_informacion, name='obtener_informacion'),
    path('video/', video, name='video'),
    path('audio/', audio, name='audio'),
]

