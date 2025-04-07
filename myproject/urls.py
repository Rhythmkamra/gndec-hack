from django.contrib import admin
from django.urls import path
from data import views as data_views  # Assuming your app is named 'data'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Default route (root URL)
    path('', data_views.register_view, name='home'),

    # Auth routes
    path('register/', data_views.register_view, name='register'),
    path('login/', data_views.login_view, name='login'),
    path('logout/', data_views.logout_view, name='logout'),

    # Student form routes
    path('cultural/', data_views.student_cultural_view, name='cultural'),
    path('sports/', data_views.student_sports_view, name='sports'),
    path('technical/', data_views.student_technical_view, name='technical'),
]
