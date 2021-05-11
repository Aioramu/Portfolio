from django.contrib import admin

# Register your models here.
from .models import Gallery,Image
# Register your models here.

admin.site.register(Image)
admin.site.register(Gallery)
