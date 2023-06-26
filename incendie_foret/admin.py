from django.contrib import admin

# Register your models here.
from .models import Foret
from .models import Incendie
admin.site.register(Foret)
admin.site.register(Incendie)