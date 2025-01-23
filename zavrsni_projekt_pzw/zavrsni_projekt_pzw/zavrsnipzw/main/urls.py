from django.urls import path, include
from . import views
from main.views import BoravisteList, PolaznikList, RasporedList, RazinaList, RezultatList, TecajList, TerminList, UciteljList
from main.views import BoravisteDetailView, PolaznikDetailView, RazinaDetailView, TecajDetailView, UciteljDetailView, TerminDetailView, RasporedDetailView, RezultatDetailView
from rest_framework.routers import DefaultRouter
from main.views import *
from main.views import BoravisteViewSet, PolaznikViewSet, RasporedViewSet, RazinaViewSet, RezultatViewSet, TecajViewSet, TerminViewSet, UciteljViewSet

app_name = 'main'  

router = DefaultRouter()
router.register(r'api/boravista', BoravisteViewSet, basename='boraviste')
router.register(r'api/polaznici', PolaznikViewSet, basename='polaznik')
router.register(r'api/rasporedi', RasporedViewSet, basename='raspored')
router.register(r'api/razine', RazinaViewSet, basename='razina')
router.register(r'api/rezultati', RezultatViewSet, basename='rezultat')
router.register(r'api/tecajevi', TecajViewSet, basename='tecaj')
router.register(r'api/termini', TerminViewSet, basename='termin')
router.register(r'api/ucitelji', UciteljViewSet, basename='ucitelj')

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),

    path('boraviste/', BoravisteList.as_view(), name='boraviste_list'),
    path('boraviste/<int:pk>/', BoravisteDetailView.as_view(), name='boraviste_detail'),
    path('addbor/', BoravisteCreateView.as_view(), name='addbor'),
    path('updatebor/<int:pk>', BoravisteUpdateView.as_view(), name='updatebor'),
    path('deletebor/<int:pk>', BoravisteDeleteView.as_view(), name='deletebor'),

    path('polaznik/', PolaznikList.as_view(), name='polaznik_list'),
    path('polaznik/<int:pk>/', PolaznikDetailView.as_view(), name='polaznik_detail'),
    path('addpol/', PolaznikCreateView.as_view(), name='addpol'),
    path('updatepol/<int:pk>', PolaznikUpdateView.as_view(), name='updatepol'),
    path('deletepol/<int:pk>', PolaznikDeleteView.as_view(), name='deletepol'),

    path('raspored/', RasporedList.as_view(), name='raspored_list'),
    path('raspored/<int:pk>/', RasporedDetailView.as_view(), name='raspored_detail'),
    path('addras/', RasporedCreateView.as_view(), name='addras'),
    path('updateras/<int:pk>', RasporedUpdateView.as_view(), name='updateras'),
    path('deleteras/<int:pk>', RasporedDeleteView.as_view(), name='deleteras'),

    path('razina/', RazinaList.as_view(), name='razina_list'),
    path('razina/<int:pk>/', RazinaDetailView.as_view(), name='razina_detail'),
    path('addraz/', RazinaCreateView.as_view(), name='addraz'),
    path('updateraz/<int:pk>', RazinaUpdateView.as_view(), name='updateraz'),
    path('deleteraz/<int:pk>', RazinaDeleteView.as_view(), name='deleteraz'),

    path('rezultat/', RezultatList.as_view(), name='rezultat_list'),
    path('rezultat/<int:pk>/', RezultatDetailView.as_view(), name='rezultat_detail'),
    path('addrez/', RezultatCreateView.as_view(), name='addrez'),
    path('updaterez/<int:pk>', RezultatUpdateView.as_view(), name='updaterez'),
    path('deleterez/<int:pk>', RezultatDeleteView.as_view(), name='deleterez'),

    path('tecaj/', TecajList.as_view(), name='tecaj_list'),
    path('tecaj/<int:pk>/', TecajDetailView.as_view(), name='tecaj_detail'),
    path('addtec/', TecajCreateView.as_view(), name='addtec'),
    path('updatetec/<int:pk>', TecajUpdateView.as_view(), name='updatetec'),
    path('deletetec/<int:pk>', TecajDeleteView.as_view(), name='deletetec'),

    path('termin/', TerminList.as_view(), name='termin_list'),
    path('termin/<int:pk>/', TerminDetailView.as_view(), name='termin_detail'),
    path('addterm/', TerminCreateView.as_view(), name='addterm'),
    path('updateterm/<int:pk>', TerminUpdateView.as_view(), name='updateterm'),
    path('deleteterm/<int:pk>', TerminDeleteView.as_view(), name='deleteterm'),

    path('ucitelj/', UciteljList.as_view(), name='ucitelj_list'),
    path('ucitelj/<int:pk>/', UciteljDetailView.as_view(), name='ucitelj_detail'),
    path('adduc/', UciteljCreateView.as_view(), name='adduc'),
    path('updateuc/<int:pk>', UciteljUpdateView.as_view(), name='updateuc'),
    path('deleteuc/<int:pk>', UciteljDeleteView.as_view(), name='deleteuc'),

    path('', include(router.urls)),  

]
