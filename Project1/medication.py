# Pre-stocked inventory
inventory = {
    'm01': {'name': 'Paracetamol', 'quantity': 100, 'expiry': '2025-12-31', 'supplier': 'MediCorp'},
    'm02': {'name': 'Amoxicillin', 'quantity': 50, 'expiry': '2024-11-15', 'supplier': 'HealthPharma'}
}

# Get medication ID first
med_id = input("Enter Medication ID: ")

# Check if medication already exists
if med_id in inventory:
    print(f"\nMedication '{med_id}' already exists in the inventory.\n")
else:
    # Continue collecting other details only if it doesn't exist
    name = input("Enter Medication Name: ")
    quantity = int(input("Enter Quantity: "))
    expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
    supplier = input("Enter Supplier Name: ")

    # Add to inventory
    inventory[med_id] = {
        'name': name,
        'quantity': quantity,
        'expiry': expiry,
        'supplier': supplier
    }

    print(f"\nMedication '{med_id}' added successfully.\n")

# Show full inventory
print("Current Medication Inventory:")
print("-" * 50)
for med, info in inventory.items():
    print(f"ID: {med}")
    print(f"  Name     : {info['name']}")
    print(f"  Quantity : {info['quantity']}")
    print(f"  Expiry   : {info['expiry']}")
    print(f"  Supplier : {info['supplier']}")
    print("-" * 50)
