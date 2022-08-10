from pyexpat import model
import re
from statistics import mode
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Species(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("species_detail", kwargs={"pk": self.id})
  

class Star(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=100)
  color = models.CharField(max_length=5)
  size = models.CharField(max_length=20)
  age = models.BigIntegerField(
    default=1000000000, 
    validators=[MinValueValidator(0), MaxValueValidator(50000000000)]
  )
  species = models.ManyToManyField(Species)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("stars_detail", kwargs={"star_id": self.id})


class Planet(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=100)
  size = models.CharField(max_length=20)
  star = models.ForeignKey(Star, on_delete=models.CASCADE)

  def __str__(self):
    return self.name