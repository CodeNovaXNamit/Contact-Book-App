# Your original dictionary with nicely formatted names
contacts = {
    "Namit": 8375976079,
    "Swarnim": 9999999999
}

# Build a lookup table: lowercase input → actual key
lower_lookup = {key.lower(): key for key in contacts}

# Get input from user (in any case)
name_input = input("Enter the name to update: ").strip().lower()

# Check if name exists
if name_input in lower_lookup:   
    actual_key = lower_lookup[name_input]
    print(actual_key)
    new_value = int(input(f"Enter new value for {actual_key}: "))
    contacts[actual_key] = new_value
    print(f"Updated {actual_key} ✅")
else:
    print("Name not found ❌")

print(contacts)