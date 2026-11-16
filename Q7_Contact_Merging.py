# Q7: Contact Merging Program

print("CONTACT MERGING PROGRAM")
print("------------------------")

contacts = [
    {
        "name": "Arun",
        "phone": "9876543210",
        "email": "arun@gmail.com"
    },

    {
        "name": "Arun Kumar",
        "phone": "9876543210",
        "email": "arunkumar@gmail.com"
    },

    {
        "name": "Priya",
        "phone": "9123456780",
        "email": "priya@gmail.com"
    },

    {
        "name": "Kumar",
        "phone": "9876543210",
        "email": "kumar@gmail.com"
    },

    {
        "name": "Divya",
        "phone": "9988776655",
        "email": "divya@gmail.com"
    }
]

merged_contacts = {}

# Process each contact
for contact in contacts:

    name = contact["name"]
    phone = contact["phone"]
    email = contact["email"]

    # Remove spaces and special characters
    clean_phone = ""

    for character in phone:
        if character.isdigit():
            clean_phone += character

    # Validate phone number
    if len(clean_phone) != 10:
        print("Invalid phone number:", phone)
        continue

    # Check whether phone number already exists
    if clean_phone not in merged_contacts:

        merged_contacts[clean_phone] = {
            "names": set(),
            "emails": set()
        }

    # Merge names and emails
    merged_contacts[clean_phone]["names"].add(name)
    merged_contacts[clean_phone]["emails"].add(email)

# Display merged contacts
print("\nMERGED CONTACT DETAILS")

for phone, details in merged_contacts.items():

    print("\nPhone Number:", phone)

    print("Names:", details["names"])

    print("Emails:", details["emails"])

print("\nTotal Original Contacts:", len(contacts))

print("Total Merged Contacts:", len(merged_contacts))