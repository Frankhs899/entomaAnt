from django.urls import path
#Importando vista del home
from .views import HomeView
#Importando vistas de descarga de archivos
from .views import ArchivosView, obtener_informacion, video, audio

urlpatterns = [
    #Pagina Home
    path('', HomeView.as_view(), name='home'),
    #Pagina de descarga de archivos
    path('archivos/', ArchivosView.as_view(), name='archivos'),
    path('obtener_informacion/', obtener_informacion, name='obtener_informacion'),
    path('video/', video, name='video'),
    path('audio/', audio, name='audio'),
]