# List to store treatment cost records
treatment_costs = []

# Function to calculate treatment cost
def calculate_treatment_cost(patient_id, treatment_plan, insurance_details):
    total_cost = sum(price for treatment, price in treatment_plan)
    discount = total_cost * (insurance_details / 100)
    final_amount = total_cost - discount

    cost_record = {
        "patient_id": patient_id,
        "treatment_plan": treatment_plan,
        "total_cost": total_cost,
        "insurance_coverage": insurance_details,
        "discount": discount,
        "final_amount": final_amount
    }

    treatment_costs.append(cost_record)
    print("\nTreatment cost calculated successfully.\n")

# Function to show all treatment cost records
def show_treatment_costs():
    for i, record in enumerate(treatment_costs, 1):
        print(f"Treatment Record {i}")
        print(f"Patient ID: {record['patient_id']}")
        print("Treatment Plan:")
        for treatment, price in record["treatment_plan"]:
            print(f"  - {treatment}: ${price}")
        print(f"Total Cost: ${record['total_cost']:.2f}")
        print(f"Insurance Coverage: {record['insurance_coverage']}%")
        print(f"Discount: ${record['discount']:.2f}")
        print(f"Final Amount to Pay: ${record['final_amount']:.2f}")
        print("-" * 30)

# Program runs once
print("--- Treatment Cost Calculator ---")
pid = input("Enter Patient ID: ")
treatments = []

while True:
    treatment_name = input("Enter treatment name (or 'done' to finish): ")
    if treatment_name.lower() == "done":
        break
    try:
        price = float(input(f"Enter cost for {treatment_name}: "))
        treatments.append((treatment_name, price))
    except ValueError:
        print("Invalid cost. Please enter a numeric value.")

try:
    insurance = float(input("Enter insurance coverage percentage (e.g., 20 for 20%): "))
    calculate_treatment_cost(pid, treatments, insurance)
    show_treatment_costs()
except ValueError:
    print("Invalid insurance coverage input.")
