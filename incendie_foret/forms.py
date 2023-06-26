from django import forms    
from .models import Incendie
from .models import Foret

class IncendieForm(forms.ModelForm):
  class Meta:
    model=Incendie
    fields = ('annee_incendie', 'numero', 'date_eclosion', 'foret_domaniale', 'commune_rurale', 'ccdrf', 'superficie_incendiee','id_foret')

class ForetForm(forms.ModelForm):
    class Meta:
        model = Foret
        fields = ['id_foret','nom', 'superficie', 'localisation', 'type', 'densite']
