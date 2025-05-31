# Pre-assigned room records
room_assignments = {
    'p01': {'room_type': 'Private', 'admission_date': '2025-05-01', 'expected_duration': '5 days'},
    'p02': {'room_type': 'Shared', 'admission_date': '2025-05-28', 'expected_duration': '3 days'}
}

# Get patient ID first
patient_id = input("Enter Patient ID: ")

# Check if patient is already assigned a room
if patient_id in room_assignments:
    print(f"\nPatient '{patient_id}' is already assigned a room.\n")
else:
    # Collect other details only if not already assigned
    room_type = input("Enter Room Type (Private/Shared): ")
    admission_date = input("Enter Admission Date (YYYY-MM-DD): ")
    expected_duration = input("Enter Expected Duration (e.g., 3 days): ")

    # Assign the room
    room_assignments[patient_id] = {
        'room_type': room_type,
        'admission_date': admission_date,
        'expected_duration': expected_duration
    }

    print(f"\nRoom assigned to patient '{patient_id}' successfully.\n")

# Show full room assignment list
print("Current Room Assignments:")
print("-" * 50)
for pid, info in room_assignments.items():
    print(f"Patient ID: {pid}")
    print(f"  Room Type        : {info['room_type']}")
    print(f"  Admission Date   : {info['admission_date']}")
    print(f"  Expected Duration: {info['expected_duration']}")
    print("-" * 50)
