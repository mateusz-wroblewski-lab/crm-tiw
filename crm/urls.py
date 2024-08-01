from django.urls import path
from . import views

urlpatterns = [
    # User list
    path('', views.home, name='home'),
    path('patient_ls/', views.patient_ls, name='patient-ls'),
]