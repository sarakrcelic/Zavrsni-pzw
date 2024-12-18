from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from main.models import Ucitelj, Razina, Tecaj, Termin, Raspored, Rezultat, Boraviste, Polaznik
from django.db.models import Q
from django.views.generic.detail import DetailView

def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:index')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)

class PolaznikList(ListView):
    model = Polaznik
    template_name = 'polaznik_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(polaznik_ime__icontains=query)
        return queryset

class PolaznikDetailView(DetailView):
    model = Polaznik
    template_name = 'main/polaznik_detail.html'

class RazinaList(ListView):
    model = Razina
    template_name = 'razina_list.html'
    #context_object_name = 'razina'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(naziv__icontains=query)
        return queryset
    
class RazinaDetailView(DetailView):
    model = Razina
    template_name = 'main/razina_detail.html'

class TecajList(ListView):
    model = Tecaj
    template_name = 'tecaj_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(tecaj_naziv__icontains=query)
        return queryset

class TecajDetailView(DetailView):
    model = Tecaj
    template_name = 'main/tecaj_detail.html'

class BoravisteList(ListView):
    model = Boraviste
    template_name = 'boraviste_list.html'
    context_object_name = 'boravista'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(boraviste_naziv_mjesta__icontains=query)
        return queryset

class BoravisteDetailView(DetailView):
    model = Boraviste
    template_name = 'main/boraviste_detail.html'

class UciteljList(ListView):
    model = Ucitelj
    template_name = 'ucitelj_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(ucitelj_ime__icontains=query)
        return queryset
    
class UciteljDetailView(DetailView):
    model = Ucitelj
    template_name = 'main/ucitelj_detail.html'

class TerminList(ListView):
    model = Termin
    template_name = 'termin_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(dan_u_tjednu__icontains=query)
        return queryset

class TerminDetailView(DetailView):
    model = Termin
    template_name = 'main/termin_detail.html'
    
class RasporedList(ListView):
    model = Raspored
    template_name = 'raspored_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            # Filtrirajte prema 'vrijeme' iz povezanog modela 'Termin'
            queryset = queryset.filter(raspored_vrijeme__vrijeme=query)
        return queryset
    
class RasporedDetailView(DetailView):
    model = Raspored
    template_name = 'main/raspored_detail.html'
    

class RezultatList(ListView):
    model = Rezultat
    template_name = 'rezultat_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(ocjena__icontains=query) | Q(ocjena__icontains=query)
            )
        return queryset

    
class RezultatDetailView(DetailView):
    model = Rezultat
    template_name = 'main/rezultat_detail.html'
    