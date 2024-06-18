from django.db import models


class ExaminationRoom(models.Model):
    number = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Examination Room {self.number} on floor {self.floor}"


class HospitalRoom(models.Model):
    number = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    is_occupied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hospital Room {self.number} on floor {self.floor}"


class Bed(models.Model):
    room = models.ForeignKey(HospitalRoom, related_name='beds', on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=10, unique=True)
    is_occupied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bed {self.bed_number} in Room {self.room.number}"


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    room = models.ForeignKey(ExaminationRoom, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('room', 'doctor', 'appointment_date')

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.last_name} and {self.patient.last_name} on {self.appointment_date}"


class HospitalStay(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField(blank=True, null=True)
    reason_for_admission = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient} staying in Bed {self.bed.bed_number} (Doctor: {self.doctor.last_name})"

    def save(self, *args, **kwargs):
        if self.discharge_date is None:
            self.bed.is_occupied = True
        else:
            self.bed.is_occupied = False
        self.bed.save()
        super().save(*args, **kwargs)
