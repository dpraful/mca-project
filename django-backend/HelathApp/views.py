from decimal import Decimal

from django.shortcuts import render,HttpResponse,redirect

from .import models

def index(request):
    return render(request,'index.html') 

from decimal import Decimal

from django.contrib import messages
from django.shortcuts import render, redirect

from . import models


def registration(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        image = request.FILES.get("image")
        address = request.POST.get("address")
        dob = request.POST.get("dob")
        district = request.POST.get("district")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        blood_group = request.POST.get("blood_group")
        emergency_contact = request.POST.get("emergency_contact")

        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        if models.reg.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("registration")

        try:
            latitude = Decimal(latitude)
            longitude = Decimal(longitude)
        except:
            latitude = None
            longitude = None

        user = models.reg.objects.create(
            name=name,
            age=age,
            gender=gender,
            email=email,
            password=password,
            phone=phone,
            image=image,
            address=address,
            dob=dob,
            district=district,
            state=state,
            pincode=pincode,
            latitude=latitude,
            longitude=longitude,
            emergency_contact=emergency_contact,
            blood_group=blood_group,
        )

        messages.success(request, "Registration Successful")
        return redirect("login")

    return render(request, "registration.html")

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            user = models.reg.objects.get(email=email)

            if user.password == password:

                if user.status == "Active":

                    # Store user details in session
                    request.session["user_id"] = user.id
                    request.session["email"] = user.email

                    return redirect("home")

                else:

                    return HttpResponse(
                        "<h3 style='color:red;text-align:center;'>"
                        "Your account has been deleted or deactivated by the administrator. "
                        "Please contact the administrator."
                        "</h3>"
                    )

            else:
                return HttpResponse("Invalid Credentials")

        except models.reg.DoesNotExist:

            return HttpResponse("User not found")

    return render(request, "login.html")

def profile(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            client=models.reg.objects.get(email=email) 
            return render(request,'profile.html' ,{'client':client})

        except models.reg.DoesNotExist:
            return HttpResponse('User not found')

    else:
        return HttpResponse('not found')


def home(request):
    return render(request,'home.html')

def editprofile(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            client=models.reg.objects.get(email=email)
            
            if request.method=="POST":
                client.name=request.POST.get('name')
                client.age=request.POST.get('age')
                client.gender=request.POST.get('gender')
                client.phone=request.POST.get('phone')
                client.address=request.POST.get('address')
                client.password=request.POST.get('password')
                client.state=request.POST.get('state')
                client.district=request.POST.get('district')
                client.pincode=request.POST.get('pincode')
                client.dob=request.POST.get('dob')
                client.blood_group=request.POST.get('blood_group')
                client.emergency_contact=request.POST.get('emergency_contact')
                client.lattiude=request.POST.get('lattiude')
                client.latitude=request.POST.get('latitude')
                client.longitude=request.POST.get('longitude')

                image=request.FILES.get('image')
                if image:
                    client.image=image

                client.save()
                return redirect('profile')
            return render(request,'editprofile.html',{'client':client}) 
        
        except models.reg.DoesNotExist:
            return HttpResponse("user not found")
    
    return HttpResponse('Not found')

def logout(request):
    if 'email' in request.session:
        request.session.flush()
        return redirect('index')
    else:
        return redirect('index') 

from decimal import Decimal
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

def Hregister(request):

    if request.method == "POST":

        hospital_name = request.POST.get("hospital_name")
        hospital_type = request.POST.get("hospital_type")
        registration_no = request.POST.get("registration_no")
        license_no = request.POST.get("license_no")

        email = request.POST.get("email")
        phone = request.POST.get("phone")

        address = request.POST.get("address")
        district = request.POST.get("district")

        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        total_beds = request.POST.get("total_beds")
        icu_beds = request.POST.get("icu_beds")

        ambulance = request.POST.get("ambulance") == "True"

        admin_name = request.POST.get("admin_name")
        admin_phone = request.POST.get("admin_phone")

        username = request.POST.get("username")
        password = request.POST.get("password")

        status = "Pending"

        if models.Hospital.objects.filter(email=email).exists():

            return HttpResponse("Email already exists")

        try:
            latitude = Decimal(latitude)
            longitude = Decimal(longitude)
        except:
            latitude = None
            longitude = None

        hospital = models.Hospital(

            hospital_name=hospital_name,
            hospital_type=hospital_type,
            registration_no=registration_no,
            license_no=license_no,

            email=email,
            phone=phone,

            address=address,
            district=district,

            latitude=latitude,
            longitude=longitude,

            total_beds=total_beds,
            icu_beds=icu_beds,

            ambulance=ambulance,

            admin_name=admin_name,
            admin_phone=admin_phone,

            username=username,
            password=password,

            status=status

        )

        hospital.save()

        return HttpResponse("""<script>alert("Hospital Registration Successful.");window.location.href="/";</script>""")

    return render(request, "Hregister.html")   
 

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username and password match the admin credentials
        if username == 'admin' and password == 'admin':
            request.session['admin_logged_in'] = True
            request.session['admin_email'] = username
            return redirect('adminhome')
        
        mess= 'Invalid credentials'
        return render(request, 'admin_login.html', {'mess': mess})
    
    return render(request, 'admin_login.html')

from django.shortcuts import render
from .models import reg
from .models import Hospital
from .models import FieldWorker
from .models import Region
from .models import Disease
from .models import DiseaseCaseReport
from .models import HealthAlert

import json
from django.db.models import Count

def adminhome(request):

    # Dashboard Cards
    total_users = reg.objects.count()

    approved_hospitals = Hospital.objects.filter(
        status="Approved"
    ).count()

    pending_hospitals = Hospital.objects.filter(
        status="Pending"
    ).count()

    total_fieldworkers = FieldWorker.objects.count()

    total_regions = Region.objects.count()

    total_diseases = Disease.objects.count()

    total_reports = DiseaseCaseReport.objects.count()

    total_alerts = HealthAlert.objects.count()


    # ----------------------------
    # Hospital Beds & ICU
    # ----------------------------

    hospitals = Hospital.objects.filter(status="Approved")

    hospital_names = []

    bed_counts = []

    icu_counts = []

    for h in hospitals:

        hospital_names.append(h.hospital_name)

        if h.total_beds and h.total_beds.isdigit():
            bed_counts.append(int(h.total_beds))
        else:
            bed_counts.append(0)

        if h.icu_beds and h.icu_beds.isdigit():
            icu_counts.append(int(h.icu_beds))
        else:
            icu_counts.append(0)


    # ----------------------------
    # Hospital Type Graph
    # ----------------------------

    government = Hospital.objects.filter(
        hospital_type="Government"
    ).count()

    private = Hospital.objects.filter(
        hospital_type="Private"
    ).count()

    clinic = Hospital.objects.filter(
        hospital_type="Clinic"
    ).count()

    medical = Hospital.objects.filter(
        hospital_type="Medical College"
    ).count()

    other = Hospital.objects.filter(
        hospital_type="Other"
    ).count()


    # ----------------------------
    # Ambulance Graph
    # ----------------------------

    ambulance_yes = Hospital.objects.filter(
        ambulance=True
    ).count()

    ambulance_no = Hospital.objects.filter(
        ambulance=False
    ).count()


    # ----------------------------
    # District Graph
    # ----------------------------

    district_data = Hospital.objects.values(
        "district"
    ).annotate(
        total=Count("id")
    )

    district_names = []

    district_count = []

    for d in district_data:

        district_names.append(d["district"])

        district_count.append(d["total"])


    # ----------------------------
    # Context
    # ----------------------------

    context = {

        # Cards

        "total_users": total_users,

        "approved_hospitals": approved_hospitals,

        "pending_hospitals": pending_hospitals,

        "total_fieldworkers": total_fieldworkers,

        "total_regions": total_regions,

        "total_diseases": total_diseases,

        "total_reports": total_reports,

        "total_alerts": total_alerts,


        # Graph 1

        "hospital_graph": json.dumps([
            approved_hospitals,
            pending_hospitals
        ]),

        # Graph 2

        "dashboard_graph": json.dumps([
            total_users,
            approved_hospitals,
            total_fieldworkers
        ]),

        # Graph 3

        "resource_graph": json.dumps([
            total_regions,
            total_diseases,
            total_reports,
            total_alerts
        ]),

        # Graph 4

        "hospital_names": json.dumps(hospital_names),

        "bed_counts": json.dumps(bed_counts),

        # Graph 5

        "icu_counts": json.dumps(icu_counts),

        # Graph 6

        "hospital_type": json.dumps([
            government,
            private,
            clinic,
            medical,
            other
        ]),

        # Graph 7

        "ambulance_data": json.dumps([
            ambulance_yes,
            ambulance_no
        ]),

        # Graph 8

        "district_names": json.dumps(district_names),

        "district_count": json.dumps(district_count),

    }

    return render(request, "adminhome.html", context)

    


def userlist(request):
    user=models.reg.objects.all()
    return render(request,'userlist.html',{'i':user})

from django.shortcuts import redirect, get_object_or_404


def delete_user(request, id):

    user = models.reg.objects.get(id=id)
    user.status = "Deleted"
    user.save()

    return redirect("userlist")

from django.shortcuts import redirect, get_object_or_404

def activate_user(request, id):

    user = get_object_or_404(reg, id=id)

    user.status = "Active"

    user.save()

    return redirect("userlist")
    
                                                
from django.shortcuts import render, redirect, get_object_or_404
# from .models import Doctor

def doctor_list(request):

    doctors = Hospital.objects.all()

    return render(
        request,
        "doctor_list.html",
        {"doctors": doctors}
    )
                
def approve_doctor(request, id):

    doctor = get_object_or_404(Hospital, id=id)

    doctor.status = "Approved"

    doctor.save()

    return redirect("doctor_list")

def reject_doctor(request, id):

    doctor = get_object_or_404(Hospital, id=id)

    doctor.status = "Rejected"

    doctor.save()

    return redirect("doctor_list")

        
                       

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hospital

def hospital_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:

            hospital = Hospital.objects.get(username=username)

            if hospital.password == password:

                if hospital.status == "Approved":

                    request.session["hospital_id"] = hospital.id
                    request.session["username"] = hospital.username
                    request.session["hospital_name"] = hospital.hospital_name

                    return redirect("hospital_home")

                else:

                    return HttpResponse(
                        "<h2 style='color:red;text-align:center;'>"
                        "Your Hospital Registration is Pending Admin Approval."
                        "</h2>"
                    )

            else:

                return HttpResponse(
                    "<h2 style='color:red;text-align:center;'>Invalid Password</h2>"
                )

        except Hospital.DoesNotExist:

            return HttpResponse(
                "<h2 style='color:red;text-align:center;'>Hospital Not Found</h2>"
            )

    return render(request, "hospital_login.html")


from django.shortcuts import render, redirect

def hospital_home(request):

    if "hospital_id" not in request.session:
        return redirect("hospital_login")

    hospital = Hospital.objects.get(id=request.session["hospital_id"])

    return render(
        request,
        "hospital_home.html",
        {"hospital": hospital}
    )


from .models import Hospital

def hospital_profile(request):

    if "hospital_id" not in request.session:

        return redirect("hospital_login")

    hospital = Hospital.objects.get(
        id=request.session["hospital_id"]
    )

    return render(
        request,
        "hospital_profile.html",
        {"hospital": hospital}
    )

def hospital_logout(request):

    request.session.flush()

    return redirect("hospital_login")

# Create your views here.

from django.shortcuts import render, redirect
from .models import Hospital,Region,Disease

def update_resources(request):

    if "hospital_id" not in request.session:
        return redirect("hospital_login")

    hospital = Hospital.objects.get(id=request.session["hospital_id"])

    if request.method == "POST":

        hospital.total_beds = request.POST.get("total_beds")
        hospital.icu_beds = request.POST.get("icu_beds")

        ambulance = request.POST.get("ambulance")

        if ambulance == "True":
            hospital.ambulance = True
        else:
            hospital.ambulance = False

        hospital.save()

        return redirect("hospital_home")

    return render(
        request,
        "update_resources.html",
        {"hospital": hospital}
    )

def add_region(request):

    if request.method=="POST":

        Region.objects.create(

            region_name=request.POST.get("region_name"),

            region_type=request.POST.get("region_type"),

            latitude=request.POST.get("latitude"),

            longitude=request.POST.get("longitude")

        )

        return redirect("region_list")

    return render(request,"add_region.html")

def region_list(request):

    regions=Region.objects.all()

    return render(
        request,
        "region_list.html",
        {"regions":regions}
    )

def edit_region(request,id):

    region=Region.objects.get(id=id)

    if request.method=="POST":

        region.region_name=request.POST.get("region_name")

        region.region_type=request.POST.get("region_type")

        region.latitude=request.POST.get("latitude")

        region.longitude=request.POST.get("longitude")

        region.save()

        return redirect("region_list")

    return render(
        request,
        "edit_region.html",
        {"region":region}
    )
def delete_region(request,id):

    region=Region.objects.get(id=id)

    region.delete()

    return redirect("region_list")

from django.shortcuts import render, redirect, get_object_or_404
from .models import Region

def edit_region(request, id):

    region = get_object_or_404(Region, id=id)

    if request.method == "POST":

        region.region_name = request.POST.get("region_name")
        region.region_type = request.POST.get("region_type")
        region.latitude = request.POST.get("latitude")
        region.longitude = request.POST.get("longitude")

        region.save()

        return redirect("region_list")

    return render(
        request,
        "edit_region.html",
        {"region": region}
    )
def add_disease(request):

    if request.method=="POST":

        Disease.objects.create(

            disease_name=request.POST.get("disease_name"),

            disease_type=request.POST.get("disease_type"),

            severity_level=request.POST.get("severity_level"),

            description=request.POST.get("description"),
            precautions=request.POST.get("precautions"),

        )

        return redirect("disease_list")

    return render(request,"add_disease.html")

def disease_list(request):

    diseases=Disease.objects.all()

    return render(
        request,
        "disease_list.html",
        {"diseases":diseases}
    )

def edit_disease(request,id):

    disease=Disease.objects.get(id=id)

    if request.method=="POST":

        disease.disease_name=request.POST.get("disease_name")

        disease.disease_type=request.POST.get("disease_type")

        disease.severity_level=request.POST.get("severity_level")

        disease.description=request.POST.get("description")
        disease.precautions=request.POST.get("precautions")

        disease.save()

        return redirect("disease_list")

    return render(
        request,
        "edit_disease.html",
        {"disease":disease}
    )


def delete_disease(request,id):

    Disease.objects.get(id=id).delete()

    return redirect("disease_list")









from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import FieldWorker
from datetime import date


def fieldworker_register(request):

    if request.method=="POST":

        full_name=request.POST.get("full_name")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        employee_id=request.POST.get("employee_id")
        department=request.POST.get("department")
        designation=request.POST.get("designation")
        district=request.POST.get("district")
        panchayat=request.POST.get("panchayat")
        ward=request.POST.get("ward")
        qualification=request.POST.get("qualification")
        experience=request.POST.get("experience")
        address=request.POST.get("address")
        username=request.POST.get("username")
        password=request.POST.get("password")


        if FieldWorker.objects.filter(email=email).exists():

            return HttpResponse("Email already exists")


        if FieldWorker.objects.filter(username=username).exists():

            return HttpResponse("Username already exists")


        if FieldWorker.objects.filter(employee_id=employee_id).exists():

            return HttpResponse("Employee ID already exists")


        birth=date.fromisoformat(dob)

        age=(date.today()-birth).days//365

        if age<18:

            return HttpResponse("Age must be above 18")


        FieldWorker.objects.create(

            full_name=full_name,

            gender=gender,

            dob=dob,

            phone=phone,

            email=email,

            employee_id=employee_id,

            department=department,

            designation=designation,

            district=district,

            panchayat=panchayat,

            ward=ward,

            qualification=qualification,

            experience=experience,

            address=address,

            username=username,

            password=password,

            status="Pending"

        )

        return HttpResponse("Registration Successful")

    return render(request,"fieldworker_register.html")

from django.shortcuts import render
from .models import FieldWorker

def worker_list(request):

    workers = FieldWorker.objects.all().order_by("-id")

    return render(
        request,
        "worker_list.html",
        {"workers": workers}
    )

from django.shortcuts import redirect, get_object_or_404
from .models import FieldWorker

def approve_worker(request, id):

    worker = get_object_or_404(FieldWorker, id=id)

    worker.status = "Approved"

    worker.save()

    return redirect("worker_list")

from django.shortcuts import redirect, get_object_or_404
from .models import FieldWorker

def reject_worker(request, id):

    worker = get_object_or_404(FieldWorker, id=id)

    worker.status = "Rejected"

    worker.save()

    return redirect("worker_list")



from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FieldWorker

def fieldworker_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            worker = FieldWorker.objects.get(username=username)

            if worker.password != password:
                return HttpResponse("<h3>Invalid Password</h3>")

            if worker.status == "Pending":
                return HttpResponse(
                    "<h3>Your account is waiting for Admin approval.</h3>"
                )

            elif worker.status == "Rejected":
                return HttpResponse(
                    "<h3>Your account has been rejected by the Admin.</h3>"
                )

            elif worker.status == "Approved":

                request.session["worker_id"] = worker.id
                request.session["worker_name"] = worker.full_name
                request.session["worker_username"] = worker.username

                return redirect("worker_home")

        except FieldWorker.DoesNotExist:

            return HttpResponse("<h3>Username not found.</h3>")

    return render(request, "fieldworker_login.html")

def worker_home(request):

    if "worker_id" not in request.session:
        return redirect("fieldworker_login")

    worker = FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    return render(
        request,
        "worker_home.html",
        {"worker": worker}
    )

def worker_logout(request):

    request.session.flush()

    return redirect("fieldworker_login")

from django.shortcuts import render, redirect
from .models import FieldWorker

def worker_profile(request):

    if "worker_id" not in request.session:
        return redirect("fieldworker_login")

    worker = FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    return render(
        request,
        "worker_profile.html",
        {"worker":worker}
    )

from django.shortcuts import render, redirect
from .models import FieldWorker

def edit_worker_profile(request):

    if "worker_id" not in request.session:
        return redirect("fieldworker_login")

    worker = FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    if request.method=="POST":

        worker.full_name=request.POST.get("full_name")
        worker.phone=request.POST.get("phone")
        worker.email=request.POST.get("email")
        worker.district=request.POST.get("district")
        worker.panchayat=request.POST.get("panchayat")
        worker.ward=request.POST.get("ward")
        worker.qualification=request.POST.get("qualification")
        worker.experience=request.POST.get("experience")
        worker.address=request.POST.get("address")

        worker.save()

        return redirect("worker_profile")

    return render(
        request,
        "edit_worker_profile.html",
        {"worker":worker}
    )


from .models import HealthAlert, Region


def add_alert(request):

    regions = Region.objects.all()

    if request.method == "POST":

        HealthAlert.objects.create(
            title=request.POST.get("title"),
            alert_type=request.POST.get("alert_type"),
            description=request.POST.get("description"),
            district_id=request.POST.get("district"),
            status="Active"
        )

        return redirect("alert_list")

    return render(
        request,
        "add_alert.html",
        {
            "regions":regions
        }
    )

def alert_list(request):

    alerts = HealthAlert.objects.all().order_by("-id")

    return render(
        request,
        "alert_list.html",
        {"alerts": alerts}
    )


def edit_alert(request, id):

    alert = get_object_or_404(HealthAlert, id=id)
    regions = Region.objects.all()

    if request.method == "POST":

        alert.title = request.POST.get("title")
        alert.alert_type = request.POST.get("alert_type")
        alert.description = request.POST.get("description")
        alert.status = request.POST.get("status")

        district_id = request.POST.get("district")
        if district_id:
            alert.district_id = district_id

        alert.save()

        return redirect("alert_list")

    return render(
        request,
        "edit_alert.html",
        {"alert": alert, "regions": regions}
    )


def delete_alert(request, id):

    alert = get_object_or_404(HealthAlert, id=id)

    alert.delete()

    return redirect("alert_list")

from .models import Mobile_Healthcare_Unit, FieldWorker, Region


def add_mobile_unit(request):

    workers = FieldWorker.objects.filter(status="Approved")

    regions = Region.objects.all()

    if request.method == "POST":

        Mobile_Healthcare_Unit.objects.create(

            vehicle_no=request.POST.get("vehicle_no"),

            driver_name=request.POST.get("driver_name"),

            field_worker_id=request.POST.get("field_worker"),

            region_id=request.POST.get("region"),

            assigned_date=request.POST.get("assigned_date"),

            remarks=request.POST.get("remarks")

        )

        return redirect("mobile_unit_list")

    return render(
        request,
        "add_mobile_unit.html",
        {
            "workers": workers,
            "regions": regions
        }
    )


def mobile_unit_list(request):

    data = Mobile_Healthcare_Unit.objects.all()

    return render(
        request,
        "mobile_unit_list.html",
        {"data": data}
    )


def edit_mobile_unit(request, id):

    unit = get_object_or_404(
        Mobile_Healthcare_Unit,
        id=id
    )

    workers = FieldWorker.objects.filter(status="Approved")

    regions = Region.objects.all()

    if request.method == "POST":

        unit.vehicle_no = request.POST.get("vehicle_no")

        unit.driver_name = request.POST.get("driver_name")

        unit.field_worker_id = request.POST.get("field_worker")

        unit.region_id = request.POST.get("region")

        unit.assigned_date = request.POST.get("assigned_date")

        unit.remarks = request.POST.get("remarks")

        unit.status = request.POST.get("status")

        unit.save()

        return redirect("mobile_unit_list")

    return render(
        request,
        "edit_mobile_unit.html",
        {
            "unit": unit,
            "workers": workers,
            "regions": regions
        }
    )


def delete_mobile_unit(request, id):

    unit = get_object_or_404(
        Mobile_Healthcare_Unit,
        id=id
    )

    unit.delete()

    return redirect("mobile_unit_list")
from django.shortcuts import render,redirect,get_object_or_404
from .models import DiseaseCaseReport

def admin_disease_reports(request):

    reports = DiseaseCaseReport.objects.all().order_by("-id")

    return render(
        request,
        "admin_disease_reports.html",
        {
            "reports":reports
        }
    )
def verify_report(request,id):

    report=get_object_or_404(
        DiseaseCaseReport,
        id=id
    )

    report.status="Verified"

    report.save()

    return redirect("admin_disease_reports")
def reject_report(request,id):

    report=get_object_or_404(
        DiseaseCaseReport,
        id=id
    )

    report.status="Rejected"

    report.save()

    return redirect("admin_disease_reports")
def delete_report_admin(request,id):

    report=get_object_or_404(
        DiseaseCaseReport,
        id=id
    )

    report.delete()

    return redirect("admin_disease_reports")

from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DiseaseCaseReport, Disease, Region, Hospital


def submit_disease_report(request):

    if "hospital_id" not in request.session:
        return redirect("hospital_login")

    hospital = Hospital.objects.get(id=request.session["hospital_id"])
    diseases = Disease.objects.all()
    regions = Region.objects.all()

    if request.method == "POST":

        # Get values
        disease = request.POST.get("disease")
        region = request.POST.get("region")
        case_count = request.POST.get("case_count")
        male_cases = request.POST.get("male_cases")
        female_cases = request.POST.get("female_cases")
        children_cases = request.POST.get("children_cases")
        report_date = request.POST.get("report_date")
        remarks = request.POST.get("remarks")

        # Check for empty required fields
        if not all([
            disease,
            region,
            case_count,
            male_cases,
            female_cases,
            children_cases,
            report_date
        ]):
            messages.error(request, "Please fill all required fields.")
            return render(
                request,
                "submit_disease_report.html",
                {
                    "diseases": diseases,
                    "regions": regions,
                },
            )

        # Convert to integers
        try:
            case_count = int(case_count)
            male_cases = int(male_cases)
            female_cases = int(female_cases)
            children_cases = int(children_cases)
        except ValueError:
            messages.error(request, "Please enter valid numbers.")
            return render(
                request,
                "submit_disease_report.html",
                {
                    "diseases": diseases,
                    "regions": regions,
                },
            )

        # Validate total
        if case_count != (male_cases + female_cases + children_cases):
            messages.error(
                request,
                "Total Cases must equal Male + Female + Children Cases."
            )
            return render(
                request,
                "submit_disease_report.html",
                {
                    "diseases": diseases,
                    "regions": regions,
                },
            )

        # Prevent future date
        if report_date > str(date.today()):
            messages.error(request, "Future dates are not allowed.")
            return render(
                request,
                "submit_disease_report.html",
                {
                    "diseases": diseases,
                    "regions": regions,
                },
            )

        # Save
        DiseaseCaseReport.objects.create(
            hospital=hospital,
            disease_id=disease,
            region_id=region,
            case_count=case_count,
            male_cases=male_cases,
            female_cases=female_cases,
            children_cases=children_cases,
            report_date=report_date,
            remarks=remarks,
        )

        messages.success(request, "Disease report submitted successfully.")
        return redirect("my_reports")

    return render(
        request,
        "submit_disease_report.html",
        {
            "diseases": diseases,
            "regions": regions,
        },
    )
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import VaccinationCampaign, Disease, Region, Hospital, FieldWorker


def add_campaign(request):

    diseases = Disease.objects.all()
    regions = Region.objects.all()
    hospitals = Hospital.objects.filter(status='Approved')
    workers = FieldWorker.objects.filter(status='Approved')

    if request.method == 'POST':

        camp_name = request.POST.get('camp_name', '').strip()
        disease_id = request.POST.get('disease')
        region_id = request.POST.get('region')
        hospital_id = request.POST.get('hospital')
        worker_id = request.POST.get('field_worker')
        camp_date = request.POST.get('camp_date')
        camp_time = request.POST.get('camp_time')
        venue = request.POST.get('venue', '').strip()
        target_population = request.POST.get('target_population')
        description = request.POST.get('description', '').strip()

        if len(camp_name) < 5:
            messages.error(request, 'Camp name must contain at least 5 characters.')

        elif len(venue) < 5:
            messages.error(request, 'Venue must contain at least 5 characters.')

        elif len(description) < 20:
            messages.error(request, 'Description must contain at least 20 characters.')

        elif int(target_population) < 1:
            messages.error(request, 'Target population must be greater than 0.')

        elif timezone.datetime.strptime(camp_date, '%Y-%m-%d').date() < timezone.now().date():
            messages.error(request, 'Camp date cannot be in the past.')

        else:

            VaccinationCampaign.objects.create(
                camp_name=camp_name,
                disease_id=disease_id,
                region_id=region_id,
                hospital_id=hospital_id,
                field_worker_id=worker_id,
                camp_date=camp_date,
                camp_time=camp_time,
                venue=venue,
                target_population=target_population,
                description=description,
            )

            messages.success(request, 'Vaccination campaign created successfully.')

            return redirect('campaign_list')

    return render(request, 'add_campaign.html', {
        'diseases': diseases,
        'regions': regions,
        'hospitals': hospitals,
        'workers': workers
    })


def campaign_list(request):

    campaigns = VaccinationCampaign.objects.all().order_by('-id')

    return render(request, 'campaign_list.html', {'campaigns': campaigns})


def edit_campaign(request, id):

    campaign = get_object_or_404(VaccinationCampaign, id=id)

    diseases = Disease.objects.all()
    regions = Region.objects.all()
    hospitals = Hospital.objects.filter(status='Approved')
    workers = FieldWorker.objects.filter(status='Approved')

    if request.method == 'POST':

        campaign.camp_name = request.POST.get('camp_name')
        campaign.disease_id = request.POST.get('disease')
        campaign.region_id = request.POST.get('region')
        campaign.hospital_id = request.POST.get('hospital')
        campaign.field_worker_id = request.POST.get('field_worker')
        campaign.camp_date = request.POST.get('camp_date')
        campaign.camp_time = request.POST.get('camp_time')
        campaign.venue = request.POST.get('venue')
        campaign.target_population = request.POST.get('target_population')
        campaign.description = request.POST.get('description')
        campaign.status = request.POST.get('status')

        campaign.save()

        messages.success(request, 'Campaign updated successfully.')

        return redirect('campaign_list')

    return render(request, 'edit_campaign.html', {
        'campaign': campaign,
        'diseases': diseases,
        'regions': regions,
        'hospitals': hospitals,
        'workers': workers
    })


def delete_campaign(request, id):

    campaign = get_object_or_404(VaccinationCampaign, id=id)

    campaign.delete()

    messages.success(request, 'Campaign deleted successfully.')

    return redirect('campaign_list')



from django.shortcuts import render, redirect, get_object_or_404
from .models import DiseaseCaseReport, Hospital


def my_reports(request):

    if "hospital_id" not in request.session:
        return redirect("hospital_login")

    hospital = Hospital.objects.get(
        id=request.session["hospital_id"]
    )

    reports = DiseaseCaseReport.objects.filter(
        hospital=hospital
    ).order_by("-id")

    return render(
        request,
        "my_reports.html",
        {
            "reports": reports
        }
    )
    
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def edit_report(request, id):

    if "hospital_id" not in request.session:
        return redirect("hospital_login")

    hospital = Hospital.objects.get(id=request.session["hospital_id"])

    report = get_object_or_404(
        DiseaseCaseReport,
        id=id,
        hospital=hospital
    )

    diseases = Disease.objects.all()
    regions = Region.objects.all()

    if request.method == "POST":

        disease = request.POST.get("disease")
        region = request.POST.get("region")
        case_count = request.POST.get("case_count")
        male_cases = request.POST.get("male_cases")
        female_cases = request.POST.get("female_cases")
        children_cases = request.POST.get("children_cases")
        report_date = request.POST.get("report_date")
        remarks = request.POST.get("remarks")

        # Check required fields
        if not all([
            disease,
            region,
            case_count,
            male_cases,
            female_cases,
            children_cases,
            report_date
        ]):
            messages.error(request, "Please fill all required fields.")
            return render(
                request,
                "edit_report.html",
                {
                    "report": report,
                    "diseases": diseases,
                    "regions": regions,
                }
            )

        # Convert to integers safely
        try:
            case_count = int(case_count)
            male_cases = int(male_cases)
            female_cases = int(female_cases)
            children_cases = int(children_cases)
        except ValueError:
            messages.error(request, "Please enter valid numbers.")
            return render(
                request,
                "edit_report.html",
                {
                    "report": report,
                    "diseases": diseases,
                    "regions": regions,
                }
            )

        # Validate total
        if case_count != (male_cases + female_cases + children_cases):
            messages.error(
                request,
                "Total Cases must equal Male + Female + Children Cases."
            )
            return render(
                request,
                "edit_report.html",
                {
                    "report": report,
                    "diseases": diseases,
                    "regions": regions,
                }
            )

        # Prevent future date
        if report_date > str(date.today()):
            messages.error(request, "Future dates are not allowed.")
            return render(
                request,
                "edit_report.html",
                {
                    "report": report,
                    "diseases": diseases,
                    "regions": regions,
                }
            )

        # Save data
        report.disease_id = disease
        report.region_id = region
        report.case_count = case_count
        report.male_cases = male_cases
        report.female_cases = female_cases
        report.children_cases = children_cases
        report.report_date = report_date
        report.remarks = remarks

        report.save()

        messages.success(request, "Report updated successfully.")
        return redirect("my_reports")

    return render(
        request,
        "edit_report.html",
        {
            "report": report,
            "diseases": diseases,
            "regions": regions,
        }
    )





def delete_report(request,id):

    report=get_object_or_404(
        DiseaseCaseReport,
        id=id
    )

    report.delete()

    return redirect("my_reports")

from django.shortcuts import render, redirect
from .models import Hospital, HealthAlert

def hospital_alerts(request):

    if "hospital_id" not in request.session:
        return redirect("hospital_login")

    hospital = Hospital.objects.get(
        id=request.session["hospital_id"]
    )

    alerts = HealthAlert.objects.filter(
        status="Active",
        district__region_name=hospital.district
    ).order_by("-created_at")

    return render(
        request,
        "hospital_alerts.html",
        {
            "alerts": alerts,
            "hospital": hospital
        }
    )
from django.shortcuts import render, redirect
from .models import VaccinationCampaign, Hospital

def hospital_campaigns(request):

    if "hospital_id" not in request.session:
        return redirect("hospital_login")

    hospital = Hospital.objects.get(
        id=request.session["hospital_id"]
    )

    campaigns = VaccinationCampaign.objects.filter(
        hospital=hospital
    ).order_by("-camp_date")

    return render(
        request,
        "hospital_campaigns.html",
        {
            "campaigns": campaigns
        }
    )
from django.shortcuts import render, redirect
from . import models

def worker_mobile_units(request):

    if "worker_id" not in request.session:
        return redirect("worker_login")

    worker = models.FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    units = models.Mobile_Healthcare_Unit.objects.filter(
        field_worker=worker
    ).order_by("-assigned_date")

    return render(
        request,
        "worker_mobile_units.html",
        {
            "worker": worker,
            "units": units
        }
    )
from django.shortcuts import render, redirect
from . import models

def worker_campaigns(request):

    if "worker_id" not in request.session:
        return redirect("worker_login")

    worker = models.FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    campaigns = models.VaccinationCampaign.objects.filter(
        field_worker=worker
    ).order_by("-camp_date")

    return render(
        request,
        "worker_campaigns.html",
        {
            "campaigns": campaigns
        }
    )
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from . import models

def submit_completion_report(request,id):

    if "worker_id" not in request.session:
        return redirect("worker_login")

    worker=models.FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    campaign=get_object_or_404(
        models.VaccinationCampaign,
        id=id,
        field_worker=worker
    )

    if campaign.status!="Completed":

        messages.error(
            request,
            "Camp must be completed before submitting report."
        )

        return redirect("worker_campaigns")

    if models.CampCompletionReport.objects.filter(
        campaign=campaign,
        worker=worker
    ).exists():

        messages.warning(
            request,
            "Completion Report Already Submitted."
        )

        return redirect("my_completion_reports")

    if request.method=="POST":

        total_people=request.POST.get("total_people")

        vaccinated_people=request.POST.get("vaccinated_people")

        health_checkups=request.POST.get("health_checkups")

        medicines_distributed=request.POST.get("medicines_distributed")

        remarks=request.POST.get("remarks")

        if not total_people.isdigit():

            messages.error(request,"Invalid Total People")

            return redirect("submit_completion_report",id=id)

        if int(vaccinated_people)>int(total_people):

            messages.error(
                request,
                "Vaccinated count cannot exceed Total People."
            )

            return redirect("submit_completion_report",id=id)

        models.CampCompletionReport.objects.create(

            campaign=campaign,

            worker=worker,

            total_people=total_people,

            vaccinated_people=vaccinated_people,

            health_checkups=health_checkups,

            medicines_distributed=medicines_distributed,

            remarks=remarks

        )

        messages.success(
            request,
            "Completion Report Submitted Successfully."
        )

        return redirect("my_completion_reports")

    return render(
        request,
        "submit_completion_report.html",
        {
            "campaign":campaign
        }
    )

def my_completion_reports(request):

    if "worker_id" not in request.session:
        return redirect("worker_login")

    worker=models.FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    reports=models.CampCompletionReport.objects.filter(
        worker=worker
    ).order_by("-submitted_on")

    return render(
        request,
        "my_completion_reports.html",
        {
            "reports":reports
        }
    )
from django.shortcuts import get_object_or_404

def edit_completion_report(request, id):

    if "worker_id" not in request.session:
        return redirect("worker_login")

    worker = models.FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    report = get_object_or_404(
        models.CampCompletionReport,
        id=id,
        worker=worker
    )

    if request.method == "POST":

        total_people = request.POST.get("total_people")
        vaccinated_people = request.POST.get("vaccinated_people")
        health_checkups = request.POST.get("health_checkups")
        medicines_distributed = request.POST.get("medicines_distributed")
        remarks = request.POST.get("remarks")

        if int(vaccinated_people) > int(total_people):

            messages.error(
                request,
                "Vaccinated count cannot exceed Total People."
            )

            return redirect(
                "edit_completion_report",
                id=id
            )

        report.total_people = total_people
        report.vaccinated_people = vaccinated_people
        report.health_checkups = health_checkups
        report.medicines_distributed = medicines_distributed
        report.remarks = remarks

        report.save()

        messages.success(
            request,
            "Report Updated Successfully."
        )

        return redirect("my_completion_reports")

    return render(
        request,
        "edit_completion_report.html",
        {
            "report": report
        }
    )
def delete_completion_report(request,id):

    if "worker_id" not in request.session:
        return redirect("worker_login")

    worker=models.FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    report=get_object_or_404(
        models.CampCompletionReport,
        id=id,
        worker=worker
    )

    report.delete()

    messages.success(
        request,
        "Report Deleted Successfully."
    )

    return redirect("my_completion_reports")
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from . import models

def update_campaign_status(request, id):

    if "worker_id" not in request.session:
        return redirect("worker_login")

    worker = models.FieldWorker.objects.get(
        id=request.session["worker_id"]
    )

    campaign = get_object_or_404(
        models.VaccinationCampaign,
        id=id,
        field_worker=worker
    )

    if campaign.status == "Scheduled":
        campaign.status = "Ongoing"

    elif campaign.status == "Ongoing":
        campaign.status = "Completed"

    else:
        messages.info(request, "Camp is already completed.")
        return redirect("worker_campaigns")

    campaign.save()

    messages.success(request, "Camp status updated successfully.")

    return redirect("worker_campaigns")

from django.shortcuts import render, redirect
from . import models


# ============================
# Worker Health Alerts
# ============================

def worker_alerts(request):

    worker_id = request.session.get("worker_id")

    if not worker_id:
        return redirect("worker_login")


    worker = models.FieldWorker.objects.get(id=worker_id)


    alerts = models.HealthAlert.objects.filter(
        district__region_name__iexact=worker.district,
        status="Active"
    ).order_by("-created_at")


    print("Worker District:", worker.district)
    print("Alerts:", alerts)


    return render(
        request,
        "worker_alerts.html",
        {
            "worker": worker,
            "alerts": alerts
        }
    )
# ============================
# Worker Assigned Region
# ============================

def worker_region(request):

    worker_id = request.session.get("worker_id")

    if not worker_id:
        return redirect("worker_login")


    worker = models.FieldWorker.objects.get(id=worker_id)


    units = models.Mobile_Healthcare_Unit.objects.filter(
        field_worker=worker
    )


    regions = models.Region.objects.filter(
        id__in=units.values("region")
    )


    return render(
        request,
        "worker_region.html",
        {
            "worker":worker,
            "regions":regions,
            "units":units
        }
    )



# ============================
# Worker Disease Reports
# ============================

def worker_disease_reports(request):

    worker_id = request.session.get("worker_id")

    if not worker_id:
        return redirect("worker_login")

    worker = models.FieldWorker.objects.get(id=worker_id)

    reports = models.DiseaseCaseReport.objects.filter(
        region=worker.region
    ).order_by("-created_at")

    return render(
        request,
        "worker_disease_reports.html",
        {
            "worker": worker,
            "reports": reports
        }
    )
    
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Survey, Region, FieldWorker


def add_survey(request):
    worker = FieldWorker.objects.get(id=request.session['worker_id'])

    if request.method == "POST":

        survey = Survey.objects.create(
            worker=worker,
            region=Region.objects.get(id=request.POST.get("region")),
            survey_date=request.POST.get("survey_date"),
            total_houses=request.POST.get("total_houses"),
            houses_visited=request.POST.get("houses_visited"),
            total_population=request.POST.get("total_population"),
            male_population=request.POST.get("male_population"),
            female_population=request.POST.get("female_population"),
            children=request.POST.get("children"),
            senior_citizens=request.POST.get("senior_citizens"),
            pregnant_women=request.POST.get("pregnant_women"),
            disabled_people=request.POST.get("disabled_people"),
            vaccinated_people=request.POST.get("vaccinated_people"),
            unvaccinated_people=request.POST.get("unvaccinated_people"),
            chronic_patients=request.POST.get("chronic_patients"),
            fever_cases=request.POST.get("fever_cases"),
            suspected_dengue=request.POST.get("suspected_dengue"),
            suspected_malaria=request.POST.get("suspected_malaria"),
            water_sources_checked=request.POST.get("water_sources_checked"),
            unsafe_water_sources=request.POST.get("unsafe_water_sources"),
            sanitation_issues=request.POST.get("sanitation_issues"),
            awareness_programs=request.POST.get("awareness_programs"),
            remarks=request.POST.get("remarks"),
        )

        messages.success(request, "Survey Added Successfully")
        return redirect("survey_list")

    regions = Region.objects.all()

    return render(request, "add_survey.html", {"regions": regions})


def survey_list(request):

    worker = FieldWorker.objects.get(id=request.session['worker_id'])

    surveys = Survey.objects.filter(worker=worker).order_by("-survey_date")

    return render(request, "survey_list.html", {"surveys": surveys})


def edit_survey(request, id):

    survey = get_object_or_404(Survey, id=id)

    if request.method == "POST":

        survey.region = Region.objects.get(id=request.POST.get("region"))
        survey.survey_date = request.POST.get("survey_date")
        survey.total_houses = request.POST.get("total_houses")
        survey.houses_visited = request.POST.get("houses_visited")
        survey.total_population = request.POST.get("total_population")
        survey.male_population = request.POST.get("male_population")
        survey.female_population = request.POST.get("female_population")
        survey.children = request.POST.get("children")
        survey.senior_citizens = request.POST.get("senior_citizens")
        survey.pregnant_women = request.POST.get("pregnant_women")
        survey.disabled_people = request.POST.get("disabled_people")
        survey.vaccinated_people = request.POST.get("vaccinated_people")
        survey.unvaccinated_people = request.POST.get("unvaccinated_people")
        survey.chronic_patients = request.POST.get("chronic_patients")
        survey.fever_cases = request.POST.get("fever_cases")
        survey.suspected_dengue = request.POST.get("suspected_dengue")
        survey.suspected_malaria = request.POST.get("suspected_malaria")
        survey.water_sources_checked = request.POST.get("water_sources_checked")
        survey.unsafe_water_sources = request.POST.get("unsafe_water_sources")
        survey.sanitation_issues = request.POST.get("sanitation_issues")
        survey.awareness_programs = request.POST.get("awareness_programs")
        survey.remarks = request.POST.get("remarks")

        survey.save()

        messages.success(request, "Survey Updated Successfully")
        return redirect("survey_list")

    regions = Region.objects.all()

    return render(request, "edit_survey.html", {
        "survey": survey,
        "regions": regions
    })


def delete_survey(request, id):

    survey = get_object_or_404(Survey, id=id)
    survey.delete()

    messages.success(request, "Survey Deleted Successfully")

    return redirect("survey_list")

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .models import (
    Disease,
    Region,
    DiseaseCaseReport,
    DiseasePrediction
)

from .arima import predict_cases

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os


def disease_prediction(request):

    diseases = Disease.objects.all()
    regions = Region.objects.all()

    if request.method == "POST":

        disease_id = request.POST.get("disease")
        region_id = request.POST.get("region")

        disease = Disease.objects.get(id=disease_id)
        region = Region.objects.get(id=region_id)

        reports = DiseaseCaseReport.objects.filter(
            disease=disease,
            region=region
        ).order_by("report_date")

        if reports.count() < 10:

            messages.error(
                request,
                "Minimum 10 disease reports required for ARIMA prediction."
            )

            return redirect("disease_prediction")

        # Convert queryset to dataframe
        df = pd.DataFrame(
            list(
                reports.values(
                    "report_date",
                    "case_count"
                )
            )
        )

        # ARIMA Prediction
        result = predict_cases(df)

        actual = result["actual"]
        predicted = result["predicted"]
        confidence = result["confidence"]

        # Delete previous prediction
        DiseasePrediction.objects.filter(
            disease=disease,
            region=region
        ).delete()

        prediction_data = []

        next_date = actual.index.max()
                # Save Prediction

        for i in range(len(predicted)):

            next_date = next_date + pd.Timedelta(days=1)

            predicted_case = float(predicted.iloc[i])

            lower = float(confidence.iloc[i, 0])

            upper = float(confidence.iloc[i, 1])

            # ==========================
            # Prediction Level
            # ==========================

            if predicted_case < 20:
                level = "Low"

            elif predicted_case < 50:
                level = "Medium"

            else:
                level = "High"

            # Save to Database

            DiseasePrediction.objects.create(

                disease=disease,

                region=region,

                prediction_date=next_date,

                predicted_cases=predicted_case,

                prediction_level=level,

                lower_confidence=lower,

                upper_confidence=upper,

                model_name="ARIMA"

            )

            # Send to Template

            prediction_data.append({

                "date": next_date,

                "cases": round(predicted_case, 2),

                "level": level,

                "lower": round(lower, 2),

                "upper": round(upper, 2)

            })
                    # ==========================
        # CREATE GRAPH
        # ==========================

        plt.figure(figsize=(12, 5))

        # Actual Cases
        plt.plot(
            actual.index,
            actual.values,
            marker="o",
            linewidth=2,
            label="Actual Cases"
        )

        # Future Dates
        future_dates = pd.date_range(
            start=actual.index.max() + pd.Timedelta(days=1),
            periods=len(predicted)
        )

        # Predicted Cases
        plt.plot(
            future_dates,
            predicted.values,
            marker="o",
            linestyle="--",
            linewidth=2,
            label="Predicted Cases"
        )

        # Confidence Interval
        plt.fill_between(
            future_dates,
            confidence.iloc[:, 0],
            confidence.iloc[:, 1],
            alpha=0.2,
            label="Confidence Interval"
        )

        # Format Date
        plt.gca().xaxis.set_major_formatter(
            mdates.DateFormatter("%d-%b")
        )

        plt.gca().xaxis.set_major_locator(
            mdates.DayLocator(interval=3)
        )

        plt.xticks(rotation=45)

        plt.xlabel("Date")
        plt.ylabel("Predicted Cases")

        plt.title(
            f"ARIMA Disease Prediction\n"
            f"{disease.disease_name} - {region.region_name}"
        )

        plt.grid(True)

        plt.legend()

        plt.tight_layout()

        # ==========================
        # SAVE GRAPH
        # ==========================

        graph_folder = os.path.join(
            settings.BASE_DIR,
            "static",
            "graphs"
        )

        os.makedirs(
            graph_folder,
            exist_ok=True
        )

        graph_path = os.path.join(
            graph_folder,
            "prediction.png"
        )

        plt.savefig(
            graph_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        # ==========================
        # RETURN RESULT
        # ==========================

        return render(
            request,
            "prediction_result.html",
            {
                "prediction": prediction_data,
                "disease": disease,
                "region": region,
                "graph": "graphs/prediction.png"
            }
        )

    return render(
        request,
        "prediction_form.html",
        {
            "diseases": diseases,
            "regions": regions
        }
    )
    
    

from .models import DiseasePrediction, Disease, Region

from django.db.models import Q

from django.shortcuts import render, redirect


from .models import DiseasePrediction, Disease, Region

def prediction_history(request):

    predictions = DiseasePrediction.objects.select_related(
        "disease",
        "region"
    ).order_by("-prediction_date")

    diseases = Disease.objects.all()

    regions = Region.objects.all()

    disease = request.GET.get("disease")

    region = request.GET.get("region")

    level = request.GET.get("level")

    if disease:

        predictions = predictions.filter(
            disease_id=disease
        )

    if region:

        predictions = predictions.filter(
            region_id=region
        )

    if level:

        predictions = predictions.filter(
            prediction_level=level
        )

    context = {

        "predictions": predictions,

        "diseases": diseases,

        "regions": regions,

        "selected_disease": disease,

        "selected_region": region,

        "selected_level": level,

    }

    return render(
        request,
        "prediction_history.html",
        context
    )

def delete_prediction(request, id):

    DiseasePrediction.objects.get(
        id=id
    ).delete()

    return redirect(
        "prediction_history"
    )


from django.db.models import Count, Avg, Max
from .models import DiseasePrediction
import matplotlib.pyplot as plt
import os
from django.conf import settings
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def prediction_dashboard(request):

    predictions = DiseasePrediction.objects.all()

    total_predictions = predictions.count()

    high_count = predictions.filter(
        prediction_level="High"
    ).count()

    medium_count = predictions.filter(
        prediction_level="Medium"
    ).count()

    low_count = predictions.filter(
        prediction_level="Low"
    ).count()


    average_cases = predictions.aggregate(
        Avg("predicted_cases")
    )["predicted_cases__avg"] or 0


    maximum_cases = predictions.aggregate(
        Max("predicted_cases")
    )["predicted_cases__max"] or 0


    top_disease = predictions.values(
        "disease__disease_name"
    ).annotate(
        total=Count("id")
    ).order_by("-total").first()


    highest_region = predictions.values(
        "region__region_name"
    ).annotate(
        total=Count("id")
    ).order_by("-total").first()


    recent_predictions = predictions.order_by(
        "-prediction_date"
    )[:10]


    # =============================
    # Trend Graph
    # =============================

    dates = predictions.order_by(
        "prediction_date"
    ).values_list(
        "prediction_date",
        flat=True
    )

    cases = predictions.order_by(
        "prediction_date"
    ).values_list(
        "predicted_cases",
        flat=True
    )


    plt.figure(figsize=(10,5))

    plt.plot(
        dates,
        cases,
        marker="o"
    )

    plt.xticks(rotation=45)

    plt.title("Prediction Trend")

    plt.xlabel("Prediction Date")

    plt.ylabel("Predicted Cases")

    plt.tight_layout()


    graph_folder = os.path.join(
        settings.BASE_DIR,
        "HelathApp",
        "static",
        "graphs"
    )

    os.makedirs(
        graph_folder,
        exist_ok=True
    )

    plt.savefig(
        os.path.join(
            graph_folder,
            "dashboard_chart.png"
        )
    )

    plt.close()


    # =============================
    # Pie Chart
    # =============================

    plt.figure(figsize=(6,6))

    plt.pie(
        [high_count, medium_count, low_count],
        labels=[
            "High",
            "Medium",
            "Low"
        ],
        autopct="%1.1f%%"
    )

    plt.title(
        "Risk Distribution"
    )

    plt.savefig(
        os.path.join(
            graph_folder,
            "pie_chart.png"
        )
    )

    plt.close()


    context = {

        "total_predictions": total_predictions,

        "high_count": high_count,

        "medium_count": medium_count,

        "low_count": low_count,

        "average_cases": round(
            average_cases,
            2
        ),

        "maximum_cases": round(
            maximum_cases,
            2
        ),

        "top_disease": top_disease,

        "highest_region": highest_region,

        "recent_predictions": recent_predictions,

        "trend_graph": "graphs/dashboard_chart.png",

        "pie_chart": "graphs/pie_chart.png",

    }

    return render(
        request,
        "prediction_dashboard.html",
        context
    )
    
from .models import HealthAlert

def user_health_alerts(request):

    alerts = HealthAlert.objects.filter(
        status="Active"
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "user_health_alerts.html",
        {
            "alerts": alerts
        }
    )

from .models import Disease

def disease_awareness(request):

    diseases = Disease.objects.all().order_by("disease_name")

    return render(
        request,
        "disease_awareness.html",
        {
            "diseases": diseases
        }
    )


def disease_details(request, id):

    disease = Disease.objects.get(id=id)

    return render(
        request,
        "disease_details.html",
        {
            "disease": disease
        }
    )

from .models import Hospital

def hospital_map(request):

    hospitals = Hospital.objects.filter(
        status="Approved"
    )

    return render(
        request,
        "hospital_map.html",
        {
            "hospitals": hospitals
        }
    )


from django.shortcuts import render
from .models import reg, VaccinationCampaign, Region


def user_campaigns(request):

    # Logged user
    user_id = request.session.get("user_id")

    user = reg.objects.get(id=user_id)


    # Dropdown search
    search = request.GET.get("region")


    # User district priority campaigns
    my_campaigns = VaccinationCampaign.objects.filter(
        region__region_name=user.district
    ).exclude(
        status="Cancelled"
    ).order_by(
        "camp_date"
    )


    # Other campaigns
    other_campaigns = VaccinationCampaign.objects.exclude(
        region__region_name=user.district
    ).exclude(
        status="Cancelled"
    ).order_by(
        "camp_date"
    )


    # Region filter
    if search:

        my_campaigns = my_campaigns.filter(
            region_id=search
        )

        other_campaigns = other_campaigns.filter(
            region_id=search
        )


    regions = Region.objects.all()


    return render(
        request,
        "user_campaigns.html",
        {
            "my_campaigns": my_campaigns,
            "other_campaigns": other_campaigns,
            "regions": regions,
            "selected": search,
            "user": user,
        }
    )




import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




def get_ai_response(message):
    # Your actual AI model/API goes here
    return "Python is a high-level programming language..."

import json
import requests

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings



import json
import requests

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def chatbot(request):

    if request.method != "POST":
        return JsonResponse(
            {"response": "Invalid request method"},
            status=405
        )

    try:
        data = json.loads(request.body)

        user_message = data.get("message", "").strip()

        if not user_message:
            return JsonResponse(
                {"response": "Please enter a message."},
                status=400
            )

        # Groq settings
        GROQ_API_KEY = settings.GROQ_API_KEY
        # CURRENT GROQ MODEL
        GROQ_MODEL = "openai/gpt-oss-120b"

        GROQ_API_URL = (
            "https://api.groq.com/openai/v1/chat/completions"
        )

        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI chatbot. "
                        "Answer questions clearly and accurately. "
                        "Keep answers simple and easy to understand."
                    )
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "temperature": 0.2,
            "max_tokens": 500
        }

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        print("Groq Status:", response.status_code)
        print("Groq Response:", response.text)

        response.raise_for_status()

        result = response.json()

        reply = result["choices"][0]["message"]["content"].strip()

        return JsonResponse({
            "response": reply
        })

    except json.JSONDecodeError:
        return JsonResponse({
            "response": "Invalid JSON received from React."
        }, status=400)

    except requests.exceptions.Timeout:
        return JsonResponse({
            "response": "Groq API request timed out."
        }, status=504)

    except requests.exceptions.HTTPError:
        return JsonResponse({
            "response": "Groq API error. Please check the API key and model."
        }, status=500)

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

        return JsonResponse({
            "response": "Could not connect to Groq."
        }, status=500)

    except Exception as e:
        print("Chatbot Error:", repr(e))

        return JsonResponse({
            "response": f"Error: {str(e)}"
        }, status=500)