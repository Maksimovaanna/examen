from django.contrib import admin
from .models import Test

# Register your models here.

class TestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Test 1', {'fields': ['field1']}),
        ('Test 2', {'fields': ['field2']}),
        ('Test 3', {'fields': ['field3']})
    ]

admin.site.register(Test, TestAdmin)