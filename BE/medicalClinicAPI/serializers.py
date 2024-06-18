from rest_framework import serializers
from .models import ExaminationRoom, HospitalRoom, Bed, Doctor, Patient, Appointment, HospitalStay


class ExaminationRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExaminationRoom
        fields = '__all__'


class HospitalRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalRoom
        fields = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class HospitalStaySerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalStay
        fields = '__all__'
