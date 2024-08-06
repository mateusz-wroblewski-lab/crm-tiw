from django.shortcuts import render, redirect
from patients.models import PatientBase
def home(request):
    return redirect('login')

def patient_ls(request):
    patient_base = PatientBase.objects.all().order_by('kons_date')
    return render(request, 'patient_ls.html', {'patient_list':patient_base})

def patient_search(request):
    # patient_base = PatientBase.objects.all()
    if request.method == 'POST':
        searched = request.POST['searched']
        patient = PatientBase.objects.all().order_by('kons_date').filter(pesnum__contains=searched)[:10]
        return render(request, 'patient_search.html', {'searched':searched, 'patient':patient})
    else:
        return render(request, 'patient_search.html', {})
