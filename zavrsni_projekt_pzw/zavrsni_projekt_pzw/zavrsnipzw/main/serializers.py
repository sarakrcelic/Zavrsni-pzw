from rest_framework import serializers
from .models import Ucitelj, Razina, Tecaj, Polaznik, Boraviste, Termin, Raspored, Rezultat

class UciteljSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ucitelj
        fields = '__all__'

class RazinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Razina
        fields = '__all__'

class TecajSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecaj
        fields = '__all__'

class PolaznikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polaznik
        fields = '__all__'

class BoravisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boraviste
        fields = '__all__'

class TerminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Termin
        fields = '__all__'

class RasporedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raspored
        fields = '__all__'

class RezultatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezultat
        fields = '__all__'
