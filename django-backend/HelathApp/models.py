from django.db import models
# Create your models here.

from django.db import models

class reg(models.Model):

    GENDER_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    ]

    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    DISTRICTS = [
        ('Thiruvananthapuram','Thiruvananthapuram'),
        ('Kollam','Kollam'),
        ('Pathanamthitta','Pathanamthitta'),
        ('Alappuzha','Alappuzha'),
        ('Kottayam','Kottayam'),
        ('Idukki','Idukki'),
        ('Ernakulam','Ernakulam'),
        ('Thrissur','Thrissur'),
        ('Palakkad','Palakkad'),
        ('Malappuram','Malappuram'),
        ('Kozhikode','Kozhikode'),
        ('Wayanad','Wayanad'),
        ('Kannur','Kannur'),
        ('Kasaragod','Kasaragod'),
    ]

    STATES = [
        ('Kerala','Kerala'),
        ('Tamil Nadu','Tamil Nadu'),
        ('Karnataka','Karnataka'),
    ]

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=100)

    phone = models.CharField(max_length=10)

    image = models.ImageField(
        upload_to="Image/",
        blank=True,
        null=True
    )

    address = models.TextField()

    dob = models.DateField()

    district = models.CharField(
        max_length=30,
        choices=DISTRICTS
    )

    state = models.CharField(
        max_length=30,
        choices=STATES
    )

    pincode = models.CharField(max_length=6)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    emergency_contact = models.CharField(max_length=10)

    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUPS
    )
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Deleted', 'Deleted'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Active"
    )

    def __str__(self):
        return self.name



class Hospital(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    ]

    HOSPITAL_TYPES = [
        ('Government', 'Government'),
        ('Private', 'Private'),
        ('Clinic', 'Clinic'),
        ('Medical College', 'Medical College'),
        ('Other', 'Other'),
    ]

    hospital_name = models.CharField(max_length=255)
    hospital_type = models.CharField(max_length=50, choices=HOSPITAL_TYPES)
    registration_no = models.CharField(max_length=100, unique=True)
    license_no = models.CharField(max_length=100, unique=True)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    address = models.TextField()
    district = models.CharField(max_length=100)

    latitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)
    longitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

    total_beds = models.CharField(max_length=10, null=True, blank=True)
    icu_beds = models.CharField(max_length=10, null=True, blank=True)

    ambulance = models.BooleanField(default=False)

    admin_name = models.CharField(max_length=150)
    admin_phone = models.CharField(max_length=15)

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Region(models.Model):

    REGION_TYPES = [
        ('Urban', 'Urban'),
        ('Rural', 'Rural'),
        ('Tribal', 'Tribal'),
    ]

    region_name = models.CharField(max_length=100)

    region_type = models.CharField(
        max_length=20,
        choices=REGION_TYPES
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )

    def __str__(self):
        return self.region_name

class Disease(models.Model):

    SEVERITY = [

        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),

    ]

    disease_name = models.CharField(max_length=100)

    disease_type = models.CharField(max_length=100)

    severity_level = models.CharField(
        max_length=20,
        choices=SEVERITY
    )

    description = models.TextField(blank=True)

    precautions = models.TextField(blank=True)

    def __str__(self):
        return self.disease_name

from django.db import models

class FieldWorker(models.Model):

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    )

    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    DISTRICTS = (
        ("Thiruvananthapuram","Thiruvananthapuram"),
        ("Kollam","Kollam"),
        ("Pathanamthitta","Pathanamthitta"),
        ("Alappuzha","Alappuzha"),
        ("Kottayam","Kottayam"),
        ("Idukki","Idukki"),
        ("Ernakulam","Ernakulam"),
        ("Thrissur","Thrissur"),
        ("Palakkad","Palakkad"),
        ("Malappuram","Malappuram"),
        ("Kozhikode","Kozhikode"),
        ("Wayanad","Wayanad"),
        ("Kannur","Kannur"),
        ("Kasaragod","Kasaragod"),
    )

    DEPARTMENT = (
        ("Disease Surveillance","Disease Surveillance"),
        ("Public Health","Public Health"),
        ("Immunization","Immunization"),
        ("Emergency Response","Emergency Response"),
        ("Health Education","Health Education"),
    )

    DESIGNATION = (
        ("Health Inspector","Health Inspector"),
        ("Junior Health Inspector","Junior Health Inspector"),
        ("Public Health Nurse","Public Health Nurse"),
        ("Field Investigator","Field Investigator"),
        ("Community Health Worker","Community Health Worker"),
    )

    full_name=models.CharField(max_length=100)

    gender=models.CharField(
        max_length=20,
        choices=GENDER
    )

    dob=models.DateField()

    phone=models.CharField(max_length=10)

    email=models.EmailField(unique=True)

    employee_id=models.CharField(
        max_length=30,
        unique=True
    )

    department=models.CharField(
        max_length=100,
        choices=DEPARTMENT
    )

    designation=models.CharField(
        max_length=100,
        choices=DESIGNATION
    )

    district=models.CharField(
        max_length=50,
        choices=DISTRICTS
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    panchayat=models.CharField(max_length=100)

    ward=models.CharField(max_length=30)

    qualification=models.CharField(max_length=100)

    experience=models.PositiveIntegerField()

    address=models.TextField()

    username=models.CharField(
        max_length=100,
        unique=True
    )

    password=models.CharField(max_length=100)

    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    def __str__(self):
        return self.full_name

class HealthAlert(models.Model):

    ALERT_TYPES = [
        ('Disease', 'Disease'),
        ('Weather', 'Weather'),
        ('Emergency', 'Emergency'),
        ('General', 'General'),
    ]

    title = models.CharField(max_length=200)

    alert_type = models.CharField(
        max_length=20,
        choices=ALERT_TYPES
    )

    description = models.TextField()

    district = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        default="Active"
    )

    def __str__(self):
        return self.title

class Mobile_Healthcare_Unit(models.Model):

    STATUS = [

        ("Assigned","Assigned"),
        ("Completed","Completed")

    ]

    vehicle_no=models.CharField(max_length=30)

    driver_name=models.CharField(max_length=100)

    field_worker=models.ForeignKey(
        FieldWorker,
        on_delete=models.CASCADE
    )

    region=models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    assigned_date=models.DateField()

    remarks=models.TextField()

    status=models.CharField(
        max_length=20,
        choices=STATUS,
        default="Assigned"
    )

    def __str__(self):
        return self.vehicle_no

class DiseaseCaseReport(models.Model):

    STATUS = [
        ("Pending", "Pending"),
        ("Verified", "Verified"),
    ]

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE
    )

    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    case_count = models.PositiveIntegerField()

    male_cases = models.PositiveIntegerField(default=0)

    female_cases = models.PositiveIntegerField(default=0)

    children_cases = models.PositiveIntegerField(default=0)

    report_date = models.DateField()

    remarks = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.disease.disease_name} - {self.hospital.hospital_name}"

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class VaccinationCampaign(models.Model):

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    camp_name = models.CharField(max_length=150)

    disease = models.ForeignKey(
        'Disease',
        on_delete=models.CASCADE
    )

    region = models.ForeignKey(
        'Region',
        on_delete=models.CASCADE
    )

    hospital = models.ForeignKey(
        'Hospital',
        on_delete=models.CASCADE
    )

    field_worker = models.ForeignKey(
        'FieldWorker',
        on_delete=models.CASCADE
    )

    camp_date = models.DateField()

    camp_time = models.TimeField()

    venue = models.CharField(max_length=250)

    target_population = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100000)
        ]
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Scheduled'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.camp_name

class CampCompletionReport(models.Model):

    campaign = models.ForeignKey(
        VaccinationCampaign,
        on_delete=models.CASCADE
    )

    worker = models.ForeignKey(
        FieldWorker,
        on_delete=models.CASCADE
    )

    total_people = models.PositiveIntegerField()

    vaccinated_people = models.PositiveIntegerField()

    health_checkups = models.PositiveIntegerField()

    medicines_distributed = models.PositiveIntegerField()

    remarks = models.TextField()

    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign.camp_name

class Survey(models.Model):

    worker = models.ForeignKey(
        FieldWorker,
        on_delete=models.CASCADE
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    survey_date = models.DateField()

    total_houses = models.PositiveIntegerField()

    houses_visited = models.PositiveIntegerField()

    total_population = models.PositiveIntegerField()

    male_population = models.PositiveIntegerField()

    female_population = models.PositiveIntegerField()

    children = models.PositiveIntegerField()

    senior_citizens = models.PositiveIntegerField()

    pregnant_women = models.PositiveIntegerField()

    disabled_people = models.PositiveIntegerField()

    vaccinated_people = models.PositiveIntegerField()

    unvaccinated_people = models.PositiveIntegerField()

    chronic_patients = models.PositiveIntegerField()

    fever_cases = models.PositiveIntegerField(default=0)

    suspected_dengue = models.PositiveIntegerField(default=0)

    suspected_malaria = models.PositiveIntegerField(default=0)

    water_sources_checked = models.PositiveIntegerField(default=0)

    unsafe_water_sources = models.PositiveIntegerField(default=0)

    sanitation_issues = models.PositiveIntegerField(default=0)

    awareness_programs = models.PositiveIntegerField(default=0)

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.region.region_name} - {self.survey_date}"


class DiseasePrediction(models.Model):

    LEVEL_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    prediction_date = models.DateField()

    predicted_cases = models.FloatField()

    prediction_level = models.CharField(
        max_length=10,
        choices=LEVEL_CHOICES,
        default="Low"
    )

    lower_confidence = models.FloatField()

    upper_confidence = models.FloatField()

    model_name = models.CharField(
        max_length=50,
        default="ARIMA"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.region} - {self.disease} - {self.prediction_level}"