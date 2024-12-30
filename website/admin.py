from django.contrib import admin
from .models import Students

# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email')  # Specify fields to display in the list view
    search_fields = ('name', 'roll_number', 'email')  # Fields to enable search functionality

# Alternatively, you can use the following line if you don't need custom admin options:
# admin.site.register(Students)
