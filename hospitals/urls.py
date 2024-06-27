
from django.contrib import admin
from django.urls import path, include
# from hospitals import views

# urlpatterns = [
#     path("", views.index, name="home"),
    
    
# ]

from hospitals.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About, name="about"),
    path('index/', Index, name="index"),
    path('',Index,name='index'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('services', services, name='services'),
    path('doctor', doctor, name='doctor'),
    path('login_form', login_form, name='login_form'),
    path('registration_form', registration_form, name='registration_form'),
    path('adminlogin', adminlogin, name='adminlogin'),
    path('admin_home', admin_home, name='admin_home'),
    path('logout', Logout, name='logout'),
    path('add_doctor', add_doctor, name='add_doctor'),
    path('view_doctor', view_doctor, name='view_doctor'),
    path('delete_doctor(?p<int:pid>)', Delete_Doctor, name='delete_doctor'),
    path('add_patient', add_patient, name='add_patient'),
    path('view_patient', view_patient, name='view_patient'),
    path('delete_patient/<int:pid>', Delete_Patient, name='delete_patient'),
    path('add_appointment', add_appointment, name='add_appointment'),
    path('view_appointment', view_appointment, name='view_appointment'),
    path('delete_appointment/<int:pid>', Delete_Appointment, name='delete_appointment'),
    path('edit_doctor/<int:pid>',edit_doctor,name='edit_doctor'),
    path('edit_patient/<int:pid>',edit_patient,name='edit_patient'),
    path('unread_queries', unread_queries, name='unread_queries'),
    path('read_queries', read_queries, name='read_queries'),
    path('view_queries/<int:pid>', view_queries, name='view_queries'),



    # tazkia login start urls section
    path('main_login_page/',main_login_page, name="main_login_page"),
    path('login_page/',login_form, name="login_from"),
    path('signup/',register_form, name="register_form"),
    path('booking/',booking, name="booking"),
    path('doctorbooking/',doctorbooking, name="doctorbooking"),
    path('testbooking/',testbooking, name="testbooking")
    # path('testbooking/',testbooking, name="testbooking")

]