from django.contrib import admin
from .models import Emp

# Custom admin configuration for the Emp model
class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'working', 'emp_id', 'phone')  # Fields to display in the admin list
    search_fields = ('name',)  # Enable search by name
    list_filter = ('working',)  # Filter by the working status

# Register the models with custom or default admin configurations
admin.site.register(Emp, EmpAdmin)  # Register Emp with EmpAdmin configuration

