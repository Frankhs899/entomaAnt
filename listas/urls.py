from django.urls import path
#Importando vista del home
from .views import ListasView

urlpatterns = [
    path('', ListasView.as_view(), name='listas'),
    # path('info_lista/', info_lista_rep, name='info_lista'),
]