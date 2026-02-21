from django.contrib import admin
from .models import Confirmation

# Register your models here.
class ConfirmationAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_confirmed')
    search_fields = ('slug',)


admin.site.register(Confirmation, ConfirmationAdmin)