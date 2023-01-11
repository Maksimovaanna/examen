from django.contrib import admin
from .models import Test, ID

# Register your models here.

class TestAdmin(admin.ModelAdmin):
    fieldsets1 = [
        ('Test 1', {'fields': ['nomer_reysa']}),
        ('Test 2', {'fields': ['aeroport_vileta']}),
        ('Test 3', {'fields': ['aeroport_prileta']}),
        ('Test 4', {'fields': ['vremya_vileta']}),
        ('Test 5', {'fields': ['dlitelnost_poleta']})
    ]

class IDAdmin(admin.ModelAdmin):
    fieldsets2 = [
        ('ID 6', {'fields': ['id_passajira']}),
        ('ID 7', {'fields': ['nomer_telefona']}),
        ('ID 8', {'fields': ['parol']}),
        ('ID 9', {'fields': ['kolichestvo_mil']})
    ]
admin.site.register(Test, TestAdmin)
admin.site.register(ID, IDAdmin)