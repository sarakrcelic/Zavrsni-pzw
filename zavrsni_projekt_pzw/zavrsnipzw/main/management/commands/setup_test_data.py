import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import (
    Ucitelj, Razina, Tecaj, Boraviste, Polaznik, Termin, Raspored, Rezultat
)
from main.factory import (
    UciteljFactory, RazinaFactory, TecajFactory, BoravisteFactory,
    PolaznikFactory, TerminFactory, RasporedFactory, RezultatFactory
)

NUM_UCITELJI = 10
NUM_RAZINE = 2  # Viša, Niža
NUM_TECAJEVI = 20
NUM_BORAVISTA = 15
NUM_POLAZNICI = 50
NUM_TERMINI = 10
NUM_REZULTATI = 100


class Command(BaseCommand):
    help = "Generates test data for the application"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Rezultat, Raspored, Termin, Polaznik, Tecaj, Razina, Boraviste, Ucitelj]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        # Generiranje učitelja
        self.stdout.write("Generating teachers...")
        ucitelji = [UciteljFactory() for _ in range(NUM_UCITELJI)]

        # Generiranje razina
        self.stdout.write("Generating levels...")
        razine = [RazinaFactory(naziv=choice) for choice in ["Viša", "Niža"]]

        # Generiranje boravišta
        self.stdout.write("Generating residences...")
        boravista = [BoravisteFactory() for _ in range(NUM_BORAVISTA)]

        # Generiranje tečajeva
        self.stdout.write("Generating courses...")
        tecajevi = [
            TecajFactory(
                tecaj_nositelj=random.choice(ucitelji),
                tecaj_razina=random.choice(razine)
            )
            for _ in range(NUM_TECAJEVI)
        ]

        # Generiranje polaznika
        self.stdout.write("Generating participants...")
        polaznici = [
            PolaznikFactory(
                polaznik_boraviste=random.choice(boravista),
                polaznik_tecaj=random.sample(tecajevi, random.randint(1, 5))
            )
            for _ in range(NUM_POLAZNICI)
        ]

        # Generiranje termina
        self.stdout.write("Generating schedules...")
        termini = [TerminFactory() for _ in range(NUM_TERMINI)]

        # Generiranje rasporeda
        self.stdout.write("Generating timetable...")
        for termin, tecaj in zip(termini, tecajevi[:NUM_TERMINI]):  # Jedan termin za određeni broj tečajeva
            RasporedFactory(vrijeme=termin, tecaj=tecaj)

        # Generiranje rezultata
        self.stdout.write("Generating results...")
        for _ in range(NUM_REZULTATI):
            RezultatFactory(
                tecaj=random.choice(tecajevi),
                polaznik=random.choice(polaznici),
                ocjena=random.choice(["A", "B", "C", "D", "F"]),
                polozen_tecaj=random.choice([True, False]),
                certifikat=random.choice([True, False]),
            )

        self.stdout.write("Test data generation complete!")
