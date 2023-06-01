from django.contrib import admin
# add Feeding to the import
from .models import Finch

admin.site.register(Finch)
# register the new Feeding Model
# admin.site.register(Feeding)
