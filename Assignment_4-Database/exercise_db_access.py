from exercise_db import do_command


def list_of_all_customers():
    return do_command("select * from customer order by customer_id")


def list_of_all_addresses():
    return do_command("select * from address order by address_id")


def address_for_customer(address_id):
    return do_command("select address from address where address_id = ?", [address_id])


def inventory_for_film(film_id):
    return do_command("select * from inventory where film_id = ?", [film_id])


def count_rentals_for_customer(customer_id):

    rentals = do_command("select count(all) as cnt  from rental where customer_id = ?", [customer_id])
    return rentals
