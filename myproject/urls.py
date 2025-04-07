from django.contrib import admin
from django.urls import path
from data import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_cultural_view, name='cultural'),
    path('sports/', views.student_sports_view, name='sports'),
    path('technical/', views.student_technical_view, name='technical'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
