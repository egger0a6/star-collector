from django.contrib import admin
from .models import Star
from .models import Planet
from .models import Species

# Register your models here.
admin.site.register(Star)
admin.site.register(Planet)
admin.site.register(Species)