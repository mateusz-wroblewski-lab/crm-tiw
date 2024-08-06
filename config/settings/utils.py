from patients.models import PatientBase, PatientProfile

def save_models(data):
    Patient_Base = PatientBase.objects.all(data)
    Patient_Profile = PatientProfile.objects.all(data)
    # Save to default
    patients_instance = [Patient_Base, Patient_Profile]
    patients_instance.save(using='default')

    patients_instance = [Patient_Base, Patient_Profile]
    patients_instance.save(using='cloudfl_db')