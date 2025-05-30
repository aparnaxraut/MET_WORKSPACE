# List to store medical records
medical_records = []

# Function to create a medical record
def create_medical_record(patient_id, doctor_id, diagnosis, treatment, prescription):
    record = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "diagnosis": diagnosis,
        "treatment": treatment,
        "prescription": prescription
    }
    medical_records.append(record)
    print("Medical record added successfully.")

# Function to show all medical records
def show_all_records():
    if not medical_records:
        print("No medical records found.")
        return
    for i, record in enumerate(medical_records, 1):
        print(f"\nRecord {i}")
        print(f"Patient ID: {record['patient_id']}")
        print(f"Doctor ID: {record['doctor_id']}")
        print(f"Diagnosis: {record['diagnosis']}")
        print(f"Treatment: {record['treatment']}")
        print(f"Prescription: {record['prescription']}")

# Sample usage
create_medical_record("P001", "D001", "Fever", "Rest and hydration", "Paracetamol 500mg")
show_all_records()
