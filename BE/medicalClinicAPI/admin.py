from django.contrib import admin
from .models import ExaminationRoom, HospitalRoom, Bed, Doctor, Patient, Appointment, HospitalStay


@admin.register(ExaminationRoom)
class ExaminationRoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'description', 'equipment', 'created_at', 'updated_at')


@admin.register(HospitalRoom)
class HospitalRoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'description', 'is_occupied', 'created_at', 'updated_at')


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ('bed_number', 'room', 'is_occupied', 'created_at', 'updated_at')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'phone_number', 'email', 'created_at', 'updated_at')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'date_of_birth', 'phone_number', 'email', 'address', 'created_at', 'updated_at')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('room', 'doctor', 'patient', 'appointment_date', 'reason', 'notes', 'created_at', 'updated_at')
    list_filter = ('appointment_date', 'doctor', 'patient', 'room')


@admin.register(HospitalStay)
class HospitalStayAdmin(admin.ModelAdmin):
    list_display = ('patient', 'bed', 'doctor', 'admission_date', 'discharge_date', 'reason_for_admission', 'notes', 'created_at', 'updated_at')
    list_filter = ('admission_date', 'discharge_date', 'doctor', 'patient', 'bed')
