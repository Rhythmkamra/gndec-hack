from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_mse_marks, name='upload_mse_marks'),
    path('my-marks/', views.my_marks, name='my_marks'),
]
