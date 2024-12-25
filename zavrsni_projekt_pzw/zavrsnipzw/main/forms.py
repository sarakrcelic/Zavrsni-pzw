from django import forms
from .models import Rezultat, Raspored, Termin, Polaznik, Boraviste, Tecaj, Razina, Ucitelj

class RezultatForm(forms.ModelForm):
    class Meta:
        model = Rezultat
        fields = '__all__'

class RasporedForm(forms.ModelForm):
    class Meta:
        model = Raspored
        fields = '__all__'

class TerminForm(forms.ModelForm):
    class Meta:
        model = Termin
        fields = '__all__'

class PolaznikForm(forms.ModelForm):
    class Meta:
        model = Polaznik
        fields = '__all__'

class BoravisteForm(forms.ModelForm):
    class Meta:
        model = Boraviste
        fields = '__all__'

class TecajForm(forms.ModelForm):
    class Meta:
        model = Tecaj
        fields = '__all__'

class RazinaForm(forms.ModelForm):
    class Meta:
        model = Razina
        fields = '__all__'

class UciteljForm(forms.ModelForm):
    class Meta:
        model = Ucitelj
        fields = '__all__'
