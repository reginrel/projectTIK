from django.contrib import admin
from django.urls import path
from faperta.views import faperta
from feb.views import feb
from fh.views import fh
from fisip.views import fisip
from fk.views import fk
from fkip.views import fkip
from ft.views import ft
from pascasarjana.views import pascasarjana
from profil.views import profil



urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', faperta),
    path('feb/', feb),
    path('fh/', fh),
    path('fisip/', fisip),
    path('fk/', fk),
    path('fkip/', fkip),
    path('ft/', ft),
    path('pascasarjana/', pascasarjana),
    path('profil/', profil),
    
]
