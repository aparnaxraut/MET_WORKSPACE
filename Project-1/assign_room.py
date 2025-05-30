# List to store room assignments
room_assignments = []

# Function to assign a room to a patient
def assign_room(patient_id, room_type, admission_date, expected_duration):
    assignment = {
        "patient_id": patient_id,
        "room_type": room_type,
        "admission_date": admission_date,
        "expected_duration": expected_duration
    }
    room_assignments.append(assignment)
    print("\nRoom assigned successfully.\n")

# Function to display all room assignments
def show_room_assignments():
    for i, room in enumerate(room_assignments, 1):
        print(f"Assignment {i}")
        print(f"Patient ID: {room['patient_id']}")
        print(f"Room Type: {room['room_type']}")
        print(f"Admission Date: {room['admission_date']}")
        print(f"Expected Duration: {room['expected_duration']} days")
        print("-" * 30)

# Program runs once
print("--- Room Assignment Entry ---")
pid = input("Enter Patient ID: ")
room = input("Enter Room Type (e.g., General, ICU, Private): ")
admission = input("Enter Admission Date (e.g., 2025-06-01): ")
duration = input("Enter Expected Duration of Stay (in days): ")

assign_room(pid, room, admission, duration)
show_room_assignments()
