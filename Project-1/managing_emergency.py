# List to store emergency admissions
emergency_admissions = []

# Function to manage emergency admission
def manage_emergency_admission(patient_id, emergency_type, severity_level):
    admission = {
        "patient_id": patient_id,
        "emergency_type": emergency_type,
        "severity_level": severity_level
    }
    emergency_admissions.append(admission)
    print("Emergency admission recorded successfully.")

# Function to show all emergency admissions
def show_emergency_admissions():
    if not emergency_admissions:
        print("No emergency admissions found.")
        return

    for i, admission in enumerate(emergency_admissions, 1):
        print(f"\nAdmission {i}")
        print(f"Patient ID: {admission['patient_id']}")
        print(f"Emergency Type: {admission['emergency_type']}")
        print(f"Severity Level: {admission['severity_level']}")

# Main program
while True:
    print("\n--- Emergency Admission System ---")
    print("1. Record Emergency Admission")
    print("2. Show All Emergency Admissions")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        pid = input("Enter Patient ID: ")
        emergency = input("Enter Emergency Type (e.g., Accident, Heart Attack): ")
        severity = input("Enter Severity Level (e.g., Mild, Moderate, Severe): ")
        manage_emergency_admission(pid, emergency, severity)
    elif choice == "2":
        show_emergency_admissions()
    elif choice == "3":
        print("Exiting the program. Stay safe!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
