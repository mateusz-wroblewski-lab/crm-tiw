from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from patients.models import PatientBase, PatientProfile
from .forms import PatientBaseForm, PatientProfileForm


# Patient flled up profile
def patient(request, patient_id):
    patient_base = PatientBase.objects.get(pk=patient_id)
    patient_profile = PatientProfile.objects.get(pk=patient_id)
    context = {
        'patient_base':patient_base,
        'patient_lab':patient_profile,
    }
    return render(request, 'patient_profile.html', context)


# Adding new patient

def patient_add(request):
    user_form = PatientBaseForm(request.POST)
    info_form = PatientProfileForm(request.POST)
    context = {
        'user_form': user_form,
        'info_form': info_form,
    }
    if all([user_form.is_valid(), info_form.is_valid()]):
        user_form.save()
        info_form.save()
        user_form = PatientBaseForm()
        info_form = PatientProfileForm()
        messages.success(request, ('Dodano pomyślnie'))
        return redirect('patient-ls')
    
    return render(request, 'patient_add.html', context)


def patient_update(request, patient_id):
    user = PatientBase.objects.get(pk=patient_id)
    info = PatientProfile.objects.get(pk=patient_id)
    user_form = PatientBaseForm(request.POST or None, instance=user)
    info_form = PatientProfileForm(request.POST or None, instance=info)
    context = {
        'user_form_update': user_form,
        'info_form_update': info_form,
    }
    if all([user_form.is_valid(), info_form.is_valid()]):
        user_form.save()
        info_form.save()
        user_form = PatientBaseForm()
        info_form = PatientProfileForm()
        messages.success(request, ('Zaktualizowano pomyślnie'))
        return redirect('patient-ls')
    
    return render(request, 'patient_update.html', context)


def patient_delete(request, patient_id):
    user = PatientBase.objects.get(pk=patient_id)
    info = PatientProfile.objects.get(pk=patient_id)
    user.delete()
    info.delete()
    messages.success(request, ('Usunięto pomyślnie'))
    return redirect('patient-ls')


