from django.urls import path
from . import views

urlpatterns = [
    # User management
    path('patient/<patient_id>/', views.patient, name='patient'),
    path('patient_add', views.patient_add, name='patient-add'),
    path('patient_update/<patient_id>', views.patient_update, name='patient-update'),
    path('patient_delete/<patient_id>', views.patient_delete, name='patient-delete'),
]