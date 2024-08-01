from django.db import models


class PatientBase(models.Model):
    GENDER_SEL = (
        ('M', 'Męska'),
        ('K', 'Żeńska'),
    )

    hcc_num = models.CharField(max_length=5, null=True)
    kons_date = models.DateField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=20, null=True)
    comment = models.TextField(max_length=300, null=True, blank=True)
    pesnum = models.IntegerField('PESEL', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_SEL, max_length=10, blank=True)
    decision = models.CharField(max_length=50, null=True, blank=True)
    leczenie = models.TextField(max_length=300, null=True, blank=True)
    grkrwi = models.CharField(max_length=15, null=True, blank=False)

    # class Meta:
    #     app_label = "patients_base"


class PatientProfile(models.Model):
    LIRADS_SEL = (
        ('1', '1'),
        ('2', '2'),
        ('2', '3'),
        ('2', '4'),
        ('2', '5'),
    )

    NASH_SEL = (
        ('Y', 'tak'),
        ('N', 'nie'),
    )

    CUKR_SEL = (
        ('Y', 'tak'),
        ('N', 'nie'),
    )

    MARSK_SEL = (
        ('Y', 'tak'),
        ('N', 'nie'),
    )

    ENCEFAL_SEL = (
        ('1/2', '1/2 stopień'),
        ('3/4', '3/4 stopień'),
    )

    WODOBRZ_SEL = (
        ('1/2', '1/2 stopień'),
        ('3/4', '3/4 stopień'),
    )

    HCV_SEL = (
        ('UJ', 'ujemne'),
        ('WYL', 'wyleczone'),
        ('DOD', 'dodatnie'),
    )

    HBV_SEL = (
        ('UJ', 'ujemne'),
        ('DOD', 'dodatnie'),
    )

    ecog = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    height = models.CharField(max_length=5, null=True, blank=True)
    weight = models.CharField(max_length=3, null=True, blank=True)
    # Details - tumor
    tumor_num = models.IntegerField(default=0, null=True, blank=True)
    tumor_place = models.TextField(max_length=30, default=0, null=True, blank=True)
    top_diameter = models.IntegerField(default=0, null=True, blank=True)
    li_rads_hcc = models.CharField(choices=LIRADS_SEL, max_length=10, blank=True)
    # Lab test
    lab_date = models.CharField(max_length=20, null=True, blank=True)
    albuminy = models.IntegerField(null=True, blank=True) # norma 3,5-5
    inr = models.IntegerField(null=True, blank=True) # norma 0,8-1,2
    kreatynina = models.IntegerField(null=True, blank=True) # norma 53–115 µmol/l (0,6–1,3 mg/dl)
    sod_surowica = models.IntegerField(null=True, blank=True) # norma 135-145 mmol/l
    bilirubina_cal = models.IntegerField(null=True, blank=True) # norma 5.1-17.1 μmol/L
    afp = models.IntegerField(null=True, blank=True) # norma od 0 do 40 µg/l
    plt = models.IntegerField(null=True, blank=True) # norma 150 tys. –400 tys
    cea = models.IntegerField(null=True, blank=True) # norma 2,5ng/ml niepalących i < 5ng/ml palących papierosy
    ca19_9 = models.IntegerField(null=True, blank=True) # < 37 U/ml
    cukrzyca = models.CharField(choices=CUKR_SEL, max_length=20, null=True, blank=True)
    nash = models.CharField(choices=NASH_SEL, max_length=20, null=True, blank=True)
    marskosc = models.CharField(choices=MARSK_SEL, max_length=20, null=True, blank=True)
    wodobrzusze = models.CharField(choices=WODOBRZ_SEL, max_length=20, null=True, blank=True)
    encefalopatia = models.CharField(choices=ENCEFAL_SEL, max_length=20, null=True, blank=True)
    hbv = models.CharField(choices=HBV_SEL, max_length=20, null=True, blank=True)
    hcv = models.CharField(choices=HCV_SEL, max_length=20, null=True, blank=True)

    # class Meta:
    #     app_label = "patients_profile"