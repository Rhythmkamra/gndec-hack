from django.contrib import admin
from .models import Student_cultural,Student_technical,Student_sports
# Register your models here.
admin.site.register(Student_cultural)
admin.site.register(Student_technical)
admin.site.register(Student_sports)