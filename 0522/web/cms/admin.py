from django.contrib import admin
from .models import me
# Register your models here.

class meAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'address')

admin.site.register(me)
