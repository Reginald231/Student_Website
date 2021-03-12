import exercise_db_access

customers = exercise_db_access.list_of_all_customers()

template = "{:<15} {:<30} {:<30} {:<40} {:<30}"
row = template.format("Customer_ID", "Last_name", "First_Name", "Address", "Number of Rentals")
print(row)


for customer in customers:
    customer_id = customer['customer_id']
    address_id = customer['address_id']
    row = template.format(customer_id, customer['last_name'], customer['first_name'],
                          exercise_db_access.address_for_customer(address_id)[0]['address'],
                          exercise_db_access.count_rentals_for_customer(customer_id)[0]['cnt'])
    print(row)
