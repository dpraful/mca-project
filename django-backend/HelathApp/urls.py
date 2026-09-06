from django.urls import path
from .import views

urlpatterns=[
   path('',views.index,name='index'),
   path('registration/',views.registration,name='registration'),
   path('login/',views.login,name='login'),
   path('profile/',views.profile,name='profile'),
   path('home/',views.home,name='home'),
   path('editprofile/',views.editprofile,name='editprofile'),
   path('logout/',views.logout,name='logout'),
   path('Hregister/',views.Hregister,name='Hregister'),
   path('adminlogin/',views.adminlogin,name='adminlogin'),
   path('adminhome/',views.adminhome,name='adminhome'),
   path('userlist/',views.userlist,name='userlist'),
   path("delete_user/<int:id>/", views.delete_user, name="delete_user"),
   path("activate_user/<int:id>/", views.activate_user, name="activate_user"),
   path("doctor_list/",views.doctor_list,name="doctor_list"),
   path("approve_doctor/<int:id>/",views.approve_doctor,name="approve_doctor"),
   path("reject_doctor/<int:id>/",views.reject_doctor,name="reject_doctor"),
   path("hospital_login/",views.hospital_login,name="hospital_login"),
   path("hospital_home/",views.hospital_home,name="hospital_home"),
   path("hospital_profile/",views.hospital_profile,name="hospital_profile"),
   path("hospital_logout/",views.hospital_logout,name="hospital_logout"),
   path("submit_disease_report/",views.submit_disease_report,name="submit_disease_report"),
   path("my_reports/",views.my_reports,name="my_reports"),
   path("edit_report/<int:id>/",views.edit_report,name="edit_report"),
   path("chatbot/", views.chatbot, name="chatbot"),
   path("delete_report/<int:id>/",views.delete_report,name="delete_report"),
   path("update_resources/",views.update_resources,name="update_resources"),
   path("hospital_alerts/",views.hospital_alerts,name="hospital_alerts"),
   path("hospital_campaigns/",views.hospital_campaigns,name="hospital_campaigns"),
   path("add_region/",views.add_region,name="add_region"),
   path("region_list/",views.region_list,name="region_list"),
   path("edit_region/<int:id>/",views.edit_region,name="edit_region"),
   path("delete_region/<int:id>/",views.delete_region,name="delete_region"),
   path("admin_disease_reports/",views.admin_disease_reports,name="admin_disease_reports"),
   path("verify_report/<int:id>/",views.verify_report,name="verify_report"),
   path("reject_report/<int:id>/",views.reject_report,name="reject_report"),
   path("delete_report_admin/<int:id>/",views.delete_report_admin,name="delete_report_admin"),
   path('add_campaign/', views.add_campaign, name='add_campaign'),
   path('campaign_list/', views.campaign_list, name='campaign_list'),
   path('edit_campaign/<int:id>/', views.edit_campaign, name='edit_campaign'),
   path('delete_campaign/<int:id>/', views.delete_campaign, name='delete_campaign'),
   path("add_disease/",views.add_disease,name="add_disease"),
   path("disease_list/",views.disease_list,name="disease_list"),
   path("edit_disease/<int:id>/",views.edit_disease,name="edit_disease"),
   path("edit_region/<int:id>/",views.edit_region,name="edit_region"),

   path("edit_disease/<int:id>/",views.edit_disease,name="edit_disease"),
   path("delete_disease/<int:id>/",views.delete_disease,name="delete_disease"),
   
   path("add_alert/", views.add_alert, name="add_alert"),
   path("alert_list/", views.alert_list, name="alert_list"),
   path("edit_alert/<int:id>/", views.edit_alert, name="edit_alert"),
   path("delete_alert/<int:id>/", views.delete_alert, name="delete_alert"),
   
   path("add_mobile_unit/",views.add_mobile_unit,name="add_mobile_unit"),
   path("mobile_unit_list/",views.mobile_unit_list,name="mobile_unit_list"),
   path("edit_mobile_unit/<int:id>/",views.edit_mobile_unit,name="edit_mobile_unit"),
   path("delete_mobile_unit/<int:id>/",views.delete_mobile_unit,name="delete_mobile_unit"),


   path("fieldworker_register/",views.fieldworker_register,name="fieldworker_register"),
   path("worker_list/",views.worker_list,name="worker_list"),
   path("approve_worker/<int:id>/",views.approve_worker,name="approve_worker"),
   path("reject_worker/<int:id>/",views.reject_worker,name="reject_worker"),
   path("fieldworker_login/",views.fieldworker_login,name="fieldworker_login" ),
   path("worker_home/",views.worker_home,name="worker_home"),
   path("worker_logout/",views.worker_logout,name="worker_logout"),
   path("worker_profile/",views.worker_profile,name="worker_profile"),
   path("edit_worker_profile/",views.edit_worker_profile,name="edit_worker_profile"),
   path("worker_mobile_units/",views.worker_mobile_units,name="worker_mobile_units"),
   path("worker_campaigns/",views.worker_campaigns,name="worker_campaigns"),
   path("submit_completion_report/<int:id>/",views.submit_completion_report,name="submit_completion_report"),
   path("my_completion_reports/",views.my_completion_reports,name="my_completion_reports"),
   path("edit_completion_report/<int:id>/",views.edit_completion_report,name="edit_completion_report"),
   path("delete_completion_report/<int:id>/",views.delete_completion_report,name="delete_completion_report"),
   path("update_campaign_status/<int:id>/",views.update_campaign_status,name="update_campaign_status"),

   
path(
    'worker-alerts/',
    views.worker_alerts,
    name="worker_alerts"
),


path(
    'worker-region/',
    views.worker_region,
    name="worker_region"
),


path(
    'worker-disease-reports/',
    views.worker_disease_reports,
    name="worker_disease_reports"
),

path("add_survey/", views.add_survey, name="add_survey"),
path("survey_list/", views.survey_list, name="survey_list"),
path("edit_survey/<int:id>/", views.edit_survey, name="edit_survey"),
path("delete_survey/<int:id>/", views.delete_survey, name="delete_survey"),




path("disease_prediction/",views.disease_prediction,name="disease_prediction"),

path(
    "prediction_history/",
    views.prediction_history,
    name="prediction_history"
),

path(
    "delete_prediction/<int:id>/",
    views.delete_prediction,
    name="delete_prediction"
),
path(
    "prediction_dashboard/",
    views.prediction_dashboard,
    name="prediction_dashboard"
),
path(
    "user_health_alerts/",
    views.user_health_alerts,
    name="user_health_alerts"
),
path(
    "disease_awareness/",
    views.disease_awareness,
    name="disease_awareness"
),

path(
    "disease_details/<int:id>/",
    views.disease_details,
    name="disease_details"
),

path(
    "hospital_map/",
    views.hospital_map,
    name="hospital_map"
),
path(
    "user_campaigns/",
    views.user_campaigns,
    name="user_campaigns"
),

]