from django.contrib import admin
from patients.models import PatientBase, PatientProfile


# admin.site.register(PatientBase)
# admin.site.register(PatientProfile)

@admin.register(PatientBase)
class PatientBase(admin.ModelAdmin):
    list_display = ['id','kons_date', 'hcc_num', 'first_name', 'last_name', 'phone', 'email', 'age', 'decision', 'comment']


@admin.register(PatientProfile)
class PatientProfile(admin.ModelAdmin):
    list_display = ['id']