#   Reginald Long
#   Assignment 5
#   CS 4308 - Internet Programming
import requests


if __name__ == "__main__":
    site = input("Enter the site you wish to send a request to: ")
    filename = input("Name the output text file: ")
    req = requests.get(site)
    req.raise_for_status()  # Raises stored HTTP error if occurred.

    print("OK")
    req_text = req.text
    print("=== BEGINNING OF HTTP RESPONSE ===")
    print(req_text)
    print("=== END OF HTTP RESPONSE ===")

    file = open(filename, "w") # Creating file object to write to.
    file.write(req_text)
    file.close()

    print("Done.")
