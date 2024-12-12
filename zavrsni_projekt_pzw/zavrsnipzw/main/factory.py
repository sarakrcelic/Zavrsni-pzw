import factory
from factory.django import DjangoModelFactory
from main.models import *

# Factory za Ucitelj
class UciteljFactory(DjangoModelFactory):
    class Meta:
        model = Ucitelj

    ucitelj_ime = factory.Faker("first_name")
    ucitelj_prezime = factory.Faker("last_name")
    ucitelj_email = factory.Faker("email")
    ucitelj_broj_sati = factory.Faker("random_int", min=10, max=40)

# Factory za Razina
class RazinaFactory(DjangoModelFactory):
    class Meta:
        model = Razina

    naziv = factory.Iterator(["Viša", "Niža"])

# Factory za Tecaj
class TecajFactory(DjangoModelFactory):
    class Meta:
        model = Tecaj

    tecaj_naziv = factory.Faker("sentence", nb_words=3)
    tecaj_sadrzaj = factory.Faker("paragraph")
    tecaj_broj_sati = factory.Faker("random_int", min=1, max=50)
    tecaj_nositelj = factory.SubFactory(UciteljFactory)
    tecaj_razina = factory.SubFactory(RazinaFactory)

# Factory za Boraviste
class BoravisteFactory(DjangoModelFactory):
    class Meta:
        model = Boraviste

    boraviste_naziv_mjesta = factory.Faker("city")
    boraviste_postanski_broj = factory.Faker("postcode")

# Factory za Polaznik
class PolaznikFactory(DjangoModelFactory):
    class Meta:
        model = Polaznik

    polaznik_ime = factory.Faker("first_name")
    polaznik_prezime = factory.Faker("last_name")
    polaznik_oib = factory.Faker("numerify", text="##########")
    polaznik_boraviste = factory.SubFactory(BoravisteFactory)

    # Dodavanje povezanih tečajeva
    @factory.post_generation
    def polaznik_tecaj(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tecaj in extracted:
                self.polaznik_tecaj.add(tecaj)

# Factory za Termin
class TerminFactory(DjangoModelFactory):
    class Meta:
        model = Termin

    dan_u_tjednu = factory.Iterator(["Ponedjeljak", "Utorak", "Srijeda", "Četvrtak", "Petak"])
    vrijeme = factory.Faker("time", pattern="%H:%M", end_datetime=None)

# Factory za Raspored
class RasporedFactory(DjangoModelFactory):
    class Meta:
        model = Raspored

    vrijeme = factory.SubFactory(TerminFactory)
    tecaj = factory.SubFactory(TecajFactory)

# Factory za Rezultat
class RezultatFactory(DjangoModelFactory):
    class Meta:
        model = Rezultat

    tecaj = factory.SubFactory(TecajFactory)
    polaznik = factory.SubFactory(PolaznikFactory)
    ocjena = factory.Faker("random_element", elements=["A", "B", "C", "D", "F"])
    polozen_tecaj = factory.Faker("boolean", chance_of_getting_true=70)
    certifikat = factory.Faker("boolean", chance_of_getting_true=50)
