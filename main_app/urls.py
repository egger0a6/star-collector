from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('stars/', views.stars_index, name='stars_index'),
  path('stars/<int:star_id>/', views.stars_detail, name='stars_detail'),
  path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
  path('stars/<int:pk>/update', views.StarUpdate.as_view(), name='stars_update'),
  path('stars/<int:pk>/delete', views.StarDelete.as_view(), name='stars_delete'),
  path('stars/<int:star_id>/add_planet/', views.add_planet, name='add_planet'),
  path('stars/<int:star_id>/assoc_species/<int:species_id>/', views.assoc_species, name='assoc_species'),
  path('species/create/', views.SpeciesCreate.as_view(), name='species_create'),
  path('species/<int:pk>/', views.SpeciesDetail.as_view(), name='species_detail'),
  path('species/', views.SpeciesList.as_view(), name='species_index'),
  path('species/<int:pk>/update/', views.SpeciesUpdate.as_view(), name='species_update'),
  path('species/<int:pk>/delete/', views.SpeciesDelete.as_view(), name='species_delete'),
  path('accounts/signup', views.signup, name='signup')
]
