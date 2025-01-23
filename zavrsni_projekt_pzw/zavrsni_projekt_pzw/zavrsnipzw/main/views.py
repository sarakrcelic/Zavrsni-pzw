from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions

from .models import (
    Ucitelj, Razina, Tecaj, Polaznik, Boraviste, Termin, Raspored, Rezultat
)
from .serializers import (
    UciteljSerializer,
    RazinaSerializer,
    TecajSerializer,
    PolaznikSerializer,
    BoravisteSerializer,
    TerminSerializer,
    RasporedSerializer,
    RezultatSerializer,
)
from .forms import (
    RezultatForm, RasporedForm, TerminForm, UciteljForm, BoravisteForm, PolaznikForm, TecajForm, RazinaForm
)


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

class PolaznikCreateView(CreateView):
    model = Polaznik
    form_class = PolaznikForm
    template_name = 'add_polaznik.html'
    success_url = reverse_lazy('main:polaznik_list')

class PolaznikUpdateView(UpdateView):
    model = Polaznik
    form_class = PolaznikForm
    template_name = 'update_polaznik.html'
    success_url = reverse_lazy('main:polaznik_list')

class PolaznikDeleteView(DeleteView):
    model = Polaznik
    template_name = 'delete_polaznik.html'
    success_url = reverse_lazy('main:polaznik_list')

class PolaznikDetailView(DetailView):
    model = Polaznik
    template_name = 'main/polaznik_detail.html'

class RazinaList(ListView):
    model = Razina
    template_name = 'razina_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(naziv__icontains=query)
        return queryset

class RazinaCreateView(CreateView):
    model = Razina
    form_class = RazinaForm
    template_name = 'add_razina.html'
    success_url = reverse_lazy('main:razina_list')

class RazinaUpdateView(UpdateView):
    model = Razina
    form_class = RazinaForm
    template_name = 'update_razina.html'
    success_url = reverse_lazy('main:razina_list')

class RazinaDeleteView(DeleteView):
    model = Razina
    template_name = 'delete_razina.html'
    success_url = reverse_lazy('main:razina_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['razina'] = self.get_object()
        return context

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

class TecajCreateView(CreateView):
    model = Tecaj
    form_class = TecajForm
    template_name = 'add_tecaj.html'
    success_url = reverse_lazy('main:tecaj_list')

class TecajUpdateView(UpdateView):
    model = Tecaj
    form_class = TecajForm
    template_name = 'update_tecaj.html'
    success_url = reverse_lazy('main:tecaj_list')

class TecajDeleteView(DeleteView):
    model = Tecaj
    template_name = 'delete_tecaj.html'
    success_url = reverse_lazy('main:tecaj_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tecaj'] = self.get_object()
        return context

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

class BoravisteCreateView(CreateView):
    model = Boraviste
    form_class = BoravisteForm
    template_name = 'add_boraviste.html'
    success_url = reverse_lazy('main:boraviste_list')

class BoravisteUpdateView(UpdateView):
    model = Boraviste
    form_class = BoravisteForm
    template_name = 'update_boraviste.html'
    success_url = reverse_lazy('main:boraviste_list')

class BoravisteDeleteView(DeleteView):
    model = Boraviste
    template_name = 'delete_boraviste.html'
    success_url = reverse_lazy('main:boraviste_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boraviste'] = self.get_object()
        return context

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

class UciteljCreateView(CreateView):
    model = Ucitelj
    form_class = UciteljForm
    template_name = 'add_ucitelj.html'
    success_url = reverse_lazy('main:ucitelj_list')

class UciteljUpdateView(UpdateView):
    model = Ucitelj
    form_class = UciteljForm
    template_name = 'update_ucitelj.html'
    success_url = reverse_lazy('main:ucitelj_list')

class UciteljDeleteView(DeleteView):
    model = Ucitelj
    template_name = 'delete_ucitelj.html'
    success_url = reverse_lazy('main:ucitelj_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ucitelj'] = self.get_object()
        return context

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

class TerminCreateView(CreateView):
    model = Termin
    form_class = TerminForm
    template_name = 'add_termin.html'
    success_url = reverse_lazy('main:termin_list')

class TerminUpdateView(UpdateView):
    model = Termin
    form_class = TerminForm
    template_name = 'update_termin.html'
    success_url = reverse_lazy('main:termin_list')

class TerminDeleteView(DeleteView):
    model = Termin
    template_name = 'delete_termin.html'
    success_url = reverse_lazy('main:termin_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['termin'] = self.get_object()
        return context

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
            queryset = queryset.filter(raspored_vrijeme__vrijeme=query)
        return queryset

class RasporedDetailView(DetailView):
    model = Raspored
    template_name = 'main/raspored_detail.html'

class RasporedCreateView(CreateView):
    model = Raspored
    form_class = RasporedForm
    template_name = 'add_raspored.html'
    success_url = reverse_lazy('main:raspored_list')

class RasporedUpdateView(UpdateView):
    model = Raspored
    form_class = RasporedForm
    template_name = 'update_raspored.html'
    success_url = reverse_lazy('main:raspored_list')

class RasporedDeleteView(DeleteView):
    model = Raspored
    template_name = 'delete_raspored.html'
    success_url = reverse_lazy('main:raspored_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['raspored'] = self.get_object()
        return context

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

class RezultatCreateView(CreateView):
    model = Rezultat
    form_class = RezultatForm
    template_name = 'add_rezultat.html'
    success_url = reverse_lazy('main:rezultat_list')

class RezultatUpdateView(UpdateView):
    model = Rezultat
    form_class = RezultatForm
    template_name = 'update_rezultat.html'
    success_url = reverse_lazy('main:rezultat_list')

class RezultatDeleteView(DeleteView):
    model = Rezultat
    template_name = 'delete_rezultat.html'
    success_url = reverse_lazy('main:rezultat_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rezultat'] = self.get_object()
        return context

class RezultatDetailView(DetailView):
    model = Rezultat
    template_name = 'main/rezultat_detail.html'


class UciteljViewSet(viewsets.ModelViewSet):
    queryset = Ucitelj.objects.all()
    serializer_class = UciteljSerializer
    permission_classes = [permissions.IsAuthenticated]

class RazinaViewSet(viewsets.ModelViewSet):
    queryset = Razina.objects.all()
    serializer_class = RazinaSerializer
    permission_classes = [permissions.IsAuthenticated]

class TecajViewSet(viewsets.ModelViewSet):
    queryset = Tecaj.objects.all()
    serializer_class = TecajSerializer
    permission_classes = [permissions.IsAuthenticated]

class PolaznikViewSet(viewsets.ModelViewSet):
    queryset = Polaznik.objects.all()
    serializer_class = PolaznikSerializer
    permission_classes = [permissions.IsAuthenticated]

class BoravisteViewSet(viewsets.ModelViewSet):
    queryset = Boraviste.objects.all()
    serializer_class = BoravisteSerializer
    permission_classes = [permissions.IsAuthenticated]

class TerminViewSet(viewsets.ModelViewSet):
    queryset = Termin.objects.all()
    serializer_class = TerminSerializer
    permission_classes = [permissions.IsAuthenticated]

class RasporedViewSet(viewsets.ModelViewSet):
    queryset = Raspored.objects.all()
    serializer_class = RasporedSerializer
    permission_classes = [permissions.IsAuthenticated]

class RezultatViewSet(viewsets.ModelViewSet):
    queryset = Rezultat.objects.all()
    serializer_class = RezultatSerializer
    permission_classes = [permissions.IsAuthenticated]
