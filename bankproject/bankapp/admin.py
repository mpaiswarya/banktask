from django.contrib import admin
from django.contrib import admin
# Register your models here.

from .models import District
# Register your models
admin.site.register(District)

from .models import Branch
admin.site.register(Branch)