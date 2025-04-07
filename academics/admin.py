from django.contrib import admin

# Register your models here.
from .models import StudentProfile, MSEMark

admin.site.register(StudentProfile)
admin.site.register(MSEMark)

# If you want to view/manage student profiles from the admin panel: