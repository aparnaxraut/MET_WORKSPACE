# List to store billing records
billing_records = []

# Function to process billing
def process_billing(patient_id, services_list, insurance_coverage):
    total_cost = sum(price for service, price in services_list)
    discount = total_cost * (insurance_coverage / 100)
    final_amount = total_cost - discount

    bill = {
        "patient_id": patient_id,
        "services": services_list,
        "total_cost": total_cost,
        "insurance_coverage": insurance_coverage,
        "discount": discount,
        "final_amount": final_amount
    }

    billing_records.append(bill)
    print("Billing processed successfully.")

# Function to display all bills
def show_all_bills():
    if not billing_records:
        print("No billing records found.")
        return

    for i, bill in enumerate(billing_records, 1):
        print(f"\nBill {i}")
        print(f"Patient ID: {bill['patient_id']}")
        print("Services:")
        for service, price in bill["services"]:
            print(f"  - {service}: ${price}")
        print(f"Total Cost: ${bill['total_cost']:.2f}")
        print(f"Insurance Coverage: {bill['insurance_coverage']}%")
        print(f"Discount: ${bill['discount']:.2f}")
        print(f"Final Amount to Pay: ${bill['final_amount']:.2f}")

# Main program
while True:
    print("\n--- Hospital Billing System ---")
    print("1. Process Billing")
    print("2. Show All Bills")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        pid = input("Enter Patient ID: ")
        services = []
        while True:
            service_name = input("Enter service name (or type 'done' to finish): ")
            if service_name.lower() == "done":
                break
            try:
                service_price = float(input(f"Enter price for {service_name}: "))
                services.append((service_name, service_price))
            except ValueError:
                print("Invalid price. Please enter a number.")
        try:
            coverage = float(input("Enter insurance coverage percentage (e.g., 20 for 20%): "))
            process_billing(pid, services, coverage)
        except ValueError:
            print("Invalid input for insurance. Please enter a number.")
    elif choice == "2":
        show_all_bills()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
