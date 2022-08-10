import requests
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Star, Species
from .forms import PlanetForm

COLORS = ['White', 'Blue', 'Red', 'Brown']

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def stars_index(request):
  stars = Star.objects.filter(user=request.user)
  return render(request, 'stars/index.html', {'stars': stars})

@login_required
def stars_detail(request, star_id):
  star = Star.objects.get(id=star_id)
  species_star_doesnt_have = Species.objects.exclude(id__in = star.species.all().values_list('id'))
  planet_form = PlanetForm()
  return render(request, 'stars/detail.html', {
    'star': star,
    'planet_form': planet_form,
    'species': species_star_doesnt_have
  })

@login_required
def add_planet(request, star_id):
  form = PlanetForm(request.POST)
  if form.is_valid():
    response_API = requests.get("https://app.pixelencounter.com/api/basic/planets?frame=13")
    response_headers = response_API.headers
    new_planet = form.save(commit=False)
    new_planet.name = response_headers["planeta-name"]
    new_planet.image = f"https://app.pixelencounter.com/api/basic/planets/{response_headers['planeta-id']}"
    new_planet.size = response_headers['planeta-size']
    new_planet.star_id = star_id
    new_planet.save()
  return redirect('stars_detail', star_id=star_id)

@login_required
def assoc_species(request, star_id, species_id):
  Star.objects.get(id=star_id).species.add(species_id)
  return redirect('stars_detail', star_id=star_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('stars_index')
    else:
      error_message = 'Invalid sign-up => try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message }
  return render(request, 'signup.html', context)


class StarCreate(LoginRequiredMixin, CreateView):
  model = Star
  fields = ['age']

  def form_valid(self, form):
    response_API = requests.get("https://app.pixelencounter.com/api/basic/stars?frame=398455")
    response_headers = response_API.headers
    form.instance.name = response_headers["planeta-name"]
    form.instance.color = COLORS[int(response_headers['planeta-sub-color-mode'])]
    form.instance.image = f"https://app.pixelencounter.com/api/basic/stars/{response_headers['planeta-id']}"
    form.instance.size = response_headers['planeta-size']
    form.instance.user = self.request.user
    return super().form_valid(form)

class StarUpdate(LoginRequiredMixin, UpdateView):
  model = Star
  fields = ['age']

class StarDelete(LoginRequiredMixin, DeleteView):
  model = Star
  success_url = '/stars/'

class SpeciesCreate(LoginRequiredMixin, CreateView):
  model = Species
  fields = ['name']

  def form_valid(self, form):
    response_API = requests.get("https://app.pixelencounter.com/api/basic/monsters/random/png?size=100")
    response_headers = response_API.headers
    form.instance.image = f"https://app.pixelencounter.com/api/basic/monsters/{response_headers['monster-id']}/png?size=100"
    return super().form_valid(form)

class SpeciesList(LoginRequiredMixin, ListView):
  model = Species

class SpeciesDetail(LoginRequiredMixin, DetailView):
  model = Species

class SpeciesUpdate(LoginRequiredMixin, UpdateView):
  model = Species
  fields = ['name']

class SpeciesDelete(LoginRequiredMixin, DeleteView):
  model = Species
  success_url = '/species/'