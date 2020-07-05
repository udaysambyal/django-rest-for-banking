from django.contrib import admin
from .models import bank,branches

# Register your models here.
admin.site.register(bank)
@admin.register(branches)
class branchesAdmin(admin.ModelAdmin):
    list_display = ('ifsc', 'bank_id', 'branch', 'city')