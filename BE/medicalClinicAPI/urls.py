from django.urls import path

from .views.examination_room_view import ExaminationRoomView
from .views.hospital_room_view import HospitalRoomView
from .views.bed_view import BedView
from .views.doctor_view import DoctorView
from .views.patient_view import PatientView
from .views.appointment_view import AppointmentView
from .views.hospital_stay_view import HospitalStayView
from .views.login import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),

    path('examination-rooms/', ExaminationRoomView.as_view(), name='examination-room-list'),
    path('examination-rooms/<int:pk>/', ExaminationRoomView.as_view(), name='examination-room-detail'),

    path('hospital-rooms/', HospitalRoomView.as_view(), name='hospital-room-list'),
    path('hospital-rooms/<int:pk>/', HospitalRoomView.as_view(), name='hospital-room-detail'),

    path('beds/', BedView.as_view(), name='bed-list'),
    path('beds/<int:pk>/', BedView.as_view(), name='bed-detail'),

    path('doctors/', DoctorView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorView.as_view(), name='doctor-detail'),

    path('patients/', PatientView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientView.as_view(), name='patient-detail'),

    path('appointments/', AppointmentView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentView.as_view(), name='appointment-detail'),

    path('hospital-stays/', HospitalStayView.as_view(), name='hospital-stay-list'),
    path('hospital-stays/<int:pk>/', HospitalStayView.as_view(), name='hospital-stay-detail'),
]
