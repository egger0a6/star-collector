import requests
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Star
from .forms import PlanetForm

COLORS = ['White', 'Blue', 'Red', 'Brown']

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stars_index(request):
  stars = Star.objects.all()
  return render(request, 'stars/index.html', {'stars': stars})

def stars_detail(request, star_id):
  star = Star.objects.get(id=star_id)
  planet_form = PlanetForm()
  return render(request, 'stars/detail.html', {
    'star': star,
    'planet_form': planet_form
  })

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


class StarCreate(CreateView):
  model = Star
  fields = ['age']

  def form_valid(self, form):
    response_API = requests.get("https://app.pixelencounter.com/api/basic/stars?frame=398455")
    response_headers = response_API.headers
    form.instance.name = response_headers["planeta-name"]
    form.instance.color = COLORS[int(response_headers['planeta-sub-color-mode'])]
    form.instance.image = f"https://app.pixelencounter.com/api/basic/stars/{response_headers['planeta-id']}"
    form.instance.size = response_headers['planeta-size']
    return super().form_valid(form)

class StarUpdate(UpdateView):
  model = Star
  fields = ['age']

class StarDelete(DeleteView):
  model = Star
  success_url = '/stars/'