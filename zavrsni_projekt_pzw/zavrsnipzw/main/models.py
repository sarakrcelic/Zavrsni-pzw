from django.db import models


class Ucitelj(models.Model):
    ucitelj_ime = models.CharField(max_length=30)
    ucitelj_prezime = models.CharField(max_length=30)
    ucitelj_email = models.EmailField()
    ucitelj_broj_sati = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.ucitelj_ime} {self.ucitelj_prezime}'


class Razina(models.Model):
    VISINA_RAZINE = [
        ('Viša', 'Viša'),
        ('Niža', 'Niža'),
    ]
    naziv = models.CharField(max_length=10, choices=VISINA_RAZINE, unique=True)

    def __str__(self):
        return self.naziv


class Tecaj(models.Model):
    tecaj_naziv = models.CharField(max_length=100)
    tecaj_sadrzaj = models.TextField()
    tecaj_broj_sati = models.CharField(max_length=10)
    tecaj_nositelj = models.ForeignKey(Ucitelj, default=1, on_delete=models.CASCADE)
    tecaj_razina = models.ForeignKey(Razina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tecaj_naziv} ({self.tecaj_razina.naziv}, broj sati: {self.tecaj_broj_sati})'


class Boraviste(models.Model):
    boraviste_naziv_mjesta = models.CharField(max_length=200)
    boraviste_postanski_broj = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.boraviste_postanski_broj} {self.boraviste_naziv_mjesta}'


class Polaznik(models.Model):
    polaznik_ime = models.CharField(max_length=25)
    polaznik_prezime = models.CharField(max_length=50)
    polaznik_oib = models.CharField(max_length=10)
    polaznik_tecaj = models.ManyToManyField(Tecaj)
    polaznik_boraviste = models.ForeignKey(Boraviste, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.polaznik_ime} {self.polaznik_prezime}'


class Termin(models.Model):
    dan_u_tjednu = models.CharField(max_length=25)
    vrijeme = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.dan_u_tjednu} {self.vrijeme}'


class Raspored(models.Model):
    raspored_vrijeme = models.OneToOneField(
        Termin,
        on_delete=models.CASCADE,
    )
    raspored_tecaj = models.OneToOneField(
        Tecaj,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f'{self.tecaj.tecaj_naziv} ({self.vrijeme.dan_u_tjednu} {self.vrijeme.vrijeme})'


class Rezultat(models.Model):
    tecaj = models.ForeignKey(Tecaj, default=1, on_delete=models.CASCADE)
    polaznik = models.ForeignKey(Polaznik, default=1, on_delete=models.CASCADE)
    ocjena = models.CharField(max_length=5)
    polozen_tecaj = models.BooleanField(default=True)
    certifikat = models.BooleanField(default=False) 
    
    def __str__(self):
        return (
            f'{self.polaznik.polaznik_ime} {self.polaznik.polaznik_prezime} '
            f'(Tecaj: {self.tecaj}, Ocjena: {self.ocjena})'
        )
