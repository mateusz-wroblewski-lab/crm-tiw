from django.shortcuts import render
from patients.models import PatientBase
def home(request):
    return render(request, 'login.html', {})

def patient_ls(request):
    patient_base = PatientBase.objects.all()
    return render(request, 'patient_ls.html', {'patient_list':patient_base})
