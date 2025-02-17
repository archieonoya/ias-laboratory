# MAC Scenario: Military Organization

# Define clearance levels and document access rules
clearance_levels = {
    "General": ["Top Secret File", "Confidential Report"],
    "Colonel": ["Confidential Report"],
    "Soldier": []
}

# Function to check access
def check_access(name, clearance, document):
    if clearance in clearance_levels and document in clearance_levels[clearance]:
        print(f"Access Granted: {name} ({clearance}) can read {document}")
    else:
        print(f"X Access Denied: {name} ({clearance}) does not have permission to access {document}")

# Main program
print("MAC Scenario: Military Organization")
name = input("Enter your name: ")
clearance = input("Enter your clearance level (General/Colonel/Soldier): ")
document = input("Enter document to access (Top Secret File/Confidential Report): ")

check_access(name, clearance, document)