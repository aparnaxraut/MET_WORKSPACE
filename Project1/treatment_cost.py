# Pre-defined treatment costs
treatment_catalog = {
    'Basic Checkup': 100,
    'Surgery': 5000,
    'Physiotherapy': 300,
    'Dental Care': 200
}

# Records of calculated costs
treatment_costs = {
    'pat001': {'treatment': 'Surgery', 'cost': 4500, 'insurance': '10% off'}
}

# Get patient ID
patient_id = input("Enter Patient ID: ")

# Check if treatment cost already exists
if patient_id in treatment_costs:
    print(f"\nTreatment cost for patient '{patient_id}' has already been calculated.\n")
else:
    # Get treatment plan
    treatment_plan = input(f"Enter Treatment Plan ({', '.join(treatment_catalog.keys())}): ")

    if treatment_plan not in treatment_catalog:
        print("\nInvalid treatment plan. Please check the available options.\n")
    else:
        base_cost = treatment_catalog[treatment_plan]

        # Get insurance discount (assuming valid input)
        discount_percent = float(input("Enter Insurance Discount (%) [e.g., 10 for 10%]: "))
        discount_amount = base_cost * (discount_percent / 100)
        final_cost = base_cost - discount_amount

        # Record treatment cost
        treatment_costs[patient_id] = {
            'treatment': treatment_plan,
            'cost': round(final_cost, 2),
            'insurance': f"{discount_percent}% off"
        }

        print(f"\nTreatment cost calculated and saved for patient '{patient_id}'.\n")

# Display all treatment cost records
print("Patient Treatment Cost Records:")
print("-" * 50)
for pid, info in treatment_costs.items():
    print(f"Patient ID      : {pid}")
    print(f"  Treatment Plan : {info['treatment']}")
    print(f"  Final Cost     : ${info['cost']}")
    print(f"  Insurance Info : {info['insurance']}")
    print("-" * 50)
