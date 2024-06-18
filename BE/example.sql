INSERT INTO "medicalClinicAPI_examinationroom" (number, floor, description, equipment, created_at, updated_at)
VALUES ('ER101', 1, 'General examination room', 'Stethoscope, BP Monitor', NOW(), NOW()),
       ('ER102', 1, 'Pediatric examination room', 'Toys, Pediatric BP Monitor', NOW(), NOW()),
       ('ER103', 1, 'Gynecology examination room', 'Ultrasound machine', NOW(), NOW()),
       ('ER201', 2, 'Orthopedic examination room', 'X-ray machine', NOW(), NOW()),
       ('ER202', 2, 'Dermatology examination room', 'Dermatoscope', NOW(), NOW()),
       ('ER203', 2, 'ENT examination room', 'Otoscope', NOW(), NOW()),
       ('ER301', 3, 'Cardiology examination room', 'ECG Machine', NOW(), NOW()),
       ('ER302', 3, 'Neurology examination room', 'EEG Machine', NOW(), NOW()),
       ('ER303', 3, 'Psychiatry examination room', 'Couch, Assessment Tools', NOW(), NOW()),
       ('ER401', 4, 'Dental examination room', 'Dental Chair, X-ray machine', NOW(), NOW());

INSERT INTO "medicalClinicAPI_hospitalroom" (number, floor, description, is_occupied, created_at, updated_at)
VALUES ('HR101', 1, 'General ward', FALSE, NOW(), NOW()),
       ('HR102', 1, 'Pediatric ward', FALSE, NOW(), NOW()),
       ('HR103', 1, 'Gynecology ward', TRUE, NOW(), NOW()),
       ('HR201', 2, 'Orthopedic ward', FALSE, NOW(), NOW()),
       ('HR202', 2, 'Dermatology ward', FALSE, NOW(), NOW()),
       ('HR203', 2, 'ENT ward', TRUE, NOW(), NOW()),
       ('HR301', 3, 'Cardiology ward', FALSE, NOW(), NOW()),
       ('HR302', 3, 'Neurology ward', TRUE, NOW(), NOW()),
       ('HR303', 3, 'Psychiatry ward', FALSE, NOW(), NOW()),
       ('HR401', 4, 'Dental ward', FALSE, NOW(), NOW());

INSERT INTO "medicalClinicAPI_bed" (room_id, bed_number, is_occupied, created_at, updated_at)
VALUES (1, 'B101', FALSE, NOW(), NOW()),
       (1, 'B102', TRUE, NOW(), NOW()),
       (2, 'B201', FALSE, NOW(), NOW()),
       (2, 'B202', TRUE, NOW(), NOW()),
       (3, 'B301', FALSE, NOW(), NOW()),
       (3, 'B302', TRUE, NOW(), NOW()),
       (4, 'B401', FALSE, NOW(), NOW()),
       (4, 'B402', TRUE, NOW(), NOW()),
       (5, 'B501', FALSE, NOW(), NOW()),
       (5, 'B502', TRUE, NOW(), NOW());

INSERT INTO "medicalClinicAPI_doctor" (first_name, last_name, specialization, phone_number, email, created_at, updated_at)
VALUES ('John', 'Doe', 'Cardiology', '1234567890', 'johndoe@example.com', NOW(), NOW()),
       ('Jane', 'Smith', 'Pediatrics', '1234567891', 'janesmith@example.com', NOW(), NOW()),
       ('Emily', 'Jones', 'Neurology', '1234567892', 'emilyjones@example.com', NOW(), NOW()),
       ('Michael', 'Brown', 'Orthopedics', '1234567893', 'michaelbrown@example.com', NOW(), NOW()),
       ('Sarah', 'Davis', 'Dermatology', '1234567894', 'sarahdavis@example.com', NOW(), NOW()),
       ('Robert', 'Wilson', 'Psychiatry', '1234567895', 'robertwilson@example.com', NOW(), NOW()),
       ('Jessica', 'Garcia', 'ENT', '1234567896', 'jessicagarcia@example.com', NOW(), NOW()),
       ('Daniel', 'Martinez', 'Gynecology', '1234567897', 'danielmartinez@example.com', NOW(), NOW()),
       ('Laura', 'Anderson', 'Dentistry', '1234567898', 'lauraanderson@example.com', NOW(), NOW()),
       ('Thomas', 'Taylor', 'General Medicine', '1234567899', 'thomastaylor@example.com', NOW(), NOW());

INSERT INTO "medicalClinicAPI_patient" (first_name, last_name, gender, date_of_birth, phone_number, email, address, created_at, updated_at)
VALUES ('Alice', 'Johnson', 'F', '1985-05-15', '0987654321', 'alicejohnson@example.com', '123 Main St', NOW(), NOW()),
       ('Bob', 'Lee', 'M', '1990-08-22', '0987654322', 'boblee@example.com', '456 Maple Ave', NOW(), NOW()),
       ('Charlie', 'Kim', 'M', '1975-11-30', '0987654323', 'charliekim@example.com', '789 Elm Rd', NOW(), NOW()),
       ('Diana', 'Clark', 'F', '1980-03-12', '0987654324', 'dianaclark@example.com', '321 Oak St', NOW(), NOW()),
       ('Edward', 'Lopez', 'M', '1960-07-25', '0987654325', 'edwardlopez@example.com', '654 Pine St', NOW(), NOW()),
       ('Fiona', 'Gonzalez', 'F', '2000-01-10', '0987654326', 'fionagonzalez@example.com', '987 Cedar Ave', NOW(), NOW()),
       ('George', 'Harris', 'M', '1955-04-05', '0987654327', 'georgeharris@example.com', '123 Birch Rd', NOW(), NOW()),
       ('Hannah', 'Scott', 'F', '1995-09-14', '0987654328', 'hannahscott@example.com', '456 Spruce St', NOW(), NOW()),
       ('Ian', 'Mitchell', 'M', '1988-12-20', '0987654329', 'ianmitchell@example.com', '789 Willow Ave', NOW(), NOW()),
       ('Jenna', 'Perez', 'F', '1978-06-18', '0987654330', 'jennaperez@example.com', '321 Redwood St', NOW(), NOW());

INSERT INTO "medicalClinicAPI_appointment" (room_id, doctor_id, patient_id, appointment_date, reason, notes, created_at, updated_at)
VALUES (1, 1, 1, '2024-06-18 09:00:00', 'Routine checkup', 'Patient in good health', NOW(), NOW()),
       (2, 2, 2, '2024-06-18 10:00:00', 'Flu symptoms', 'Prescribed medication', NOW(), NOW()),
       (3, 3, 3, '2024-06-18 11:00:00', 'Headache', 'Further tests needed', NOW(), NOW()),
       (4, 4, 4, '2024-06-18 12:00:00', 'Back pain', 'Recommended physiotherapy', NOW(), NOW()),
       (5, 5, 5, '2024-06-18 13:00:00', 'Skin rash', 'Prescribed ointment', NOW(), NOW()),
       (6, 6, 6, '2024-06-18 14:00:00', 'Anxiety', 'Follow-up in a month', NOW(), NOW()),
       (7, 7, 7, '2024-06-18 15:00:00', 'Ear pain', 'Prescribed antibiotics', NOW(), NOW()),
       (8, 8, 8, '2024-06-18 16:00:00', 'Pregnancy checkup', 'All normal', NOW(), NOW()),
       (9, 9, 9, '2024-06-18 17:00:00', 'Toothache', 'Scheduled extraction', NOW(), NOW()),
       (10, 10, 10, '2024-06-18 18:00:00', 'General checkup', 'No issues found', NOW(), NOW());

INSERT INTO "medicalClinicAPI_hospitalstay" (patient_id, bed_id, doctor_id, admission_date, discharge_date, reason_for_admission, notes, created_at, updated_at)
VALUES (1, 1, 1, '2024-06-15 10:00:00', NULL, 'Routine observation', 'Patient stable', NOW(), NOW()),
       (2, 2, 2, '2024-06-16 11:00:00', NULL, 'Severe flu', 'Patient recovering', NOW(), NOW()),
       (3, 3, 3, '2024-06-17 12:00:00', NULL, 'Migraine', 'Under observation', NOW(), NOW()),
       (4, 4, 4, '2024-06-18 13:00:00', NULL, 'Fracture', 'Surgery scheduled', NOW(), NOW()),
       (5, 5, 5, '2024-06-19 14:00:00', NULL, 'Dermatitis', 'Applying ointment', NOW(), NOW()),
       (6, 6, 6, '2024-06-20 15:00:00', NULL, 'Anxiety', 'Monitoring', NOW(), NOW()),
       (7, 7, 7, '2024-06-21 16:00:00', NULL, 'Ear infection', 'Antibiotics prescribed', NOW(), NOW()),
       (8, 8, 8, '2024-06-22 17:00:00', NULL, 'Pregnancy', 'Regular checkups', NOW(), NOW()),
       (9, 9, 9, '2024-06-23 18:00:00', NULL, 'Tooth decay', 'Extraction scheduled', NOW(), NOW()),
       (10, 10, 10, '2024-06-24 19:00:00', NULL, 'General observation', 'No issues found', NOW(), NOW());
