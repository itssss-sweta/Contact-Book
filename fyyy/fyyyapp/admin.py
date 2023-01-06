from django.contrib import admin
from .models import Contact
# Register your models here.
class Contactdmin(admin.ModelAdmin):
    list_display=("FirstName","LastName","Email","Phone")
admin.site.register(Contact,Contactdmin)