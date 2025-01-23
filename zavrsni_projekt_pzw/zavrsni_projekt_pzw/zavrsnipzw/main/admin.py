from django.contrib import admin
from .models import *

model_list = [Ucitelj, Tecaj, Termin, Razina, Raspored, Polaznik, Rezultat, Boraviste]
admin.site.register(model_list)