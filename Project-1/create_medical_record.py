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

# Main program
while True:
    print("\n--- Hospital Medical Record System ---")
    print("1. Add Medical Record")
    print("2. Show All Records")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        pid = input("Enter Patient ID: ")
        did = input("Enter Doctor ID: ")
        diag = input("Enter Diagnosis: ")
        treat = input("Enter Treatment: ")
        pres = input("Enter Prescription: ")
        create_medical_record(pid, did, diag, treat, pres)
    elif choice == "2":
        show_all_records()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
