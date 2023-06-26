from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone

class Foret(models.Model):
    id_foret = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    superficie = models.FloatField()
    localisation = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    densite = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.nom

class Incendie(models.Model):
    id_incendie = models.AutoField(primary_key=True)
    annee_incendie = models.IntegerField()
    numero = models.CharField(max_length=100) 
    date_eclosion = models.DateField(default=timezone.now)
    foret_domaniale = models.CharField(max_length=100)
    commune_rurale = models.CharField(max_length=100)
    ccdrf = models.CharField(max_length=100)
    superficie_incendiee = models.FloatField()
    id_foret = models.ForeignKey(Foret, on_delete=models.CASCADE)

    def publish(self):
        self.date_eclosion = timezone.now()
        self.save()

    def __str__(self):
        return str(self.annee_incendie)

