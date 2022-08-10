from django.forms import ModelForm
from .models import Planet

class PlanetForm(ModelForm):
  class Meta:
    model = Planet
    fields = []