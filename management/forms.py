from django import forms
from django.forms import ModelForm
from patients.models import PatientBase, PatientProfile

class PatientBaseForm(ModelForm):
    class Meta:
        model = PatientBase
        fields = ('hcc_num', 'kons_date', 'first_name', 'last_name', 'phone', 'email',
                  'comment', 'pesnum', 'gender', 'age', 'patweight', 'patheight', 'decision', 'leczenie', 'grkrwi')

        widgets = {
            'hcc_num': forms.TextInput(attrs={'class':'form-control border border-warning text-warning', 'placeholder':'HCC'}),
            'kons_date': forms.DateInput(attrs={'class':'form-control border border-warning', 'placeholder':'rok-mieś-dzień'}),
            'first_name': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Imię'}),
            'last_name': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Nazwisko'}),
            'grkrwi': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Gr. krwi'}),
            'phone': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'+00 000-000-000'}),
            'email': forms.EmailInput(attrs={'class':'form-control border border-light', 'placeholder':'Email'}),
            'comment': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Dodaj dodatkowe uwagi'}),
            'pesnum': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'PESEL'}),
            'age': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Wiek'}),
            'patheight': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Wzrost'}),
            'patweight': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Waga'}),
            'gender': forms.Select(attrs={'class':'form-control border border-warning'}),
            'decision': forms.TextInput(attrs={'class':'form-control', 'placeholder':'decyzja'}),
            'leczenie': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Leczenie dotychczasowe:  1-Resekcja | 2-Ablacja(RFA/MWA) | 3-TACE | 4-OLTx | 5-Y90 | 6-Radioterapia | 7-Leczenie systemowe '}),
         }
        
class PatientProfileForm(ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('lab_date','ecog', 'height', 'weight', 'tumor_num', 'tumor_place', 'top_diameter', 'li_rads_hcc',
                  'albuminy', 'inr', 'kreatynina', 'sod_surowica', 'bilirubina_cal', 'afp', 'plt', 'cea', 'ca19_9',
                  'cukrzyca', 'marskosc', 'wodobrzusze', 'encefalopatia', 'hbv', 'hcv',
                  )

        widgets = {
            'lab_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'rok-mieś-dzień'}),
            'ecog': forms.TextInput(attrs={'class':'form-control', 'placeholder':'0'}),
            'height': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Wzrost'}),
            'weight': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Waga'}),
            
            # Tumor section
            'tumor_num': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Liczba guzów'}),
            'tumor_place': forms.Textarea(attrs={'class':'form-control', 'rows':1, 'placeholder':'np. 0:0'}),
            'top_diameter': forms.TextInput(attrs={'class':'form-control', 'placeholder':'np. 10 (mm)'}),
            'li_rads_hcc': forms.Select(attrs={'class':'form-control'}),
            # Lab test
            'albuminy': forms.TextInput(attrs={'class':'form-control', 'placeholder':'3,5-5'}),  # norma 3,5-5
            'inr': forms.TextInput(attrs={'class':'form-control', 'placeholder':'0,8-1,2'}),  # norma 0,8-1,2
            'kreatynina': forms.TextInput(attrs={'class':'form-control', 'placeholder':'53–115 µmol/l'}), # norma 53–115 µmol/l (0,6–1,3 mg/dl)
            'sod_surowica': forms.TextInput(attrs={'class':'form-control', 'placeholder':'135-145 mmol/l'}), # norma 135-145 mmol/l
            'bilirubina_cal': forms.TextInput(attrs={'class':'form-control w-100', 'placeholder':'5.1-17.1 μmol/L'}),  # norma 5.1-17.1 μmol/L
            'afp': forms.TextInput(attrs={'class':'form-control', 'placeholder':'0-40 µg/l'}),
            'plt': forms.TextInput(attrs={'class':'form-control', 'placeholder':'150–400 tyś'}),
            'cea': forms.TextInput(attrs={'class':'form-control', 'placeholder':'2,5ng/ml|5ng/ml'}),
            'ca19_9': forms.TextInput(attrs={'class':'form-control', 'placeholder':'< 37 U/ml'}),
            'cukrzyca': forms.Select(attrs={'class':'form-control'}),
            'marskosc': forms.Select(attrs={'class':'form-control'}),
            'wodobrzusze': forms.Select(attrs={'class':'form-control'}),
            'encefalopatia': forms.Select(attrs={'class':'form-control'}),
            'hbv': forms.Select(attrs={'class':'form-control'}),
            'hcv': forms.Select(attrs={'class':'form-control'}),
        }