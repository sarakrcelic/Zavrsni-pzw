from django.urls import path
from . import views
from main.views import BoravisteList, PolaznikList, RasporedList, RazinaList, RezultatList, TecajList, TerminList, UciteljList
from main.views import BoravisteDetailView, PolaznikDetailView, RazinaDetailView, TecajDetailView, UciteljDetailView, TerminDetailView, RasporedDetailView, RezultatDetailView

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),

    path('boraviste/', BoravisteList.as_view(), name='boraviste_list'),
    path('boraviste/<int:pk>/',BoravisteDetailView.as_view(), name='boraviste_detail'),

    path('polaznik/', PolaznikList.as_view(), name='polaznik_list'),
    path('polaznik/<int:pk>/', PolaznikDetailView.as_view(), name='polaznik_detail'),

    path('raspored/', RasporedList.as_view(), name='raspored_list'),
    path('raspored/<int:pk>/', RasporedDetailView.as_view(), name='raspored_detail'),

    path('razina/', RazinaList.as_view(), name='razina_list'),
    path('razina/<int:pk>/', RazinaDetailView.as_view(), name='razina_detail'),

    path('rezultat/', RezultatList.as_view(), name='rezultat_list'),
    path('rezultat/<int:pk>/', RezultatDetailView.as_view(), name='rezultat_detail'),

    path('tecaj/', TecajList.as_view(), name ='tecaj_list'),
    path('tecaj/<int:pk>/', TecajDetailView.as_view(), name='tecaj_detail'),

    path('termin/', TerminList.as_view(), name='termin_list'),
    path('termin/<int:pk>/', TerminDetailView.as_view(), name='termin_detail'),

    path('ucitelj/', UciteljList.as_view(), name='ucitelj_list' ),
    path('ucitelj/<int:pk>/', UciteljDetailView.as_view(), name='ucitelj_detail'),
]