# List to store medication inventory
medication_inventory = []

# Function to track medication
def track_medication_inventory(medication_id, quantity, expiry_date, supplier):
    medication = {
        "medication_id": medication_id,
        "quantity": quantity,
        "expiry_date": expiry_date,
        "supplier": supplier
    }
    medication_inventory.append(medication)
    print("\nMedication inventory updated successfully.\n")

# Function to show all medications in inventory
def show_medication_inventory():
    for i, med in enumerate(medication_inventory, 1):
        print(f"Medication {i}")
        print(f"Medication ID: {med['medication_id']}")
        print(f"Quantity: {med['quantity']}")
        print(f"Expiry Date: {med['expiry_date']}")
        print(f"Supplier: {med['supplier']}")
        print("-" * 30)

# Program runs once
print("--- Medication Inventory Entry ---")
med_id = input("Enter Medication ID: ")
qty = input("Enter Quantity: ")
expiry = input("Enter Expiry Date (e.g., 2025-12-31): ")
supplier = input("Enter Supplier Name: ")

track_medication_inventory(med_id, qty, expiry, supplier)
show_medication_inventory()
