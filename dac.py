# DAC Scenario: Simple File System

# Dictionary to store files and their permissions
files = {}

# Function to create a file with permissions
def create_file(owner):
    filename = input("Enter filename to create: ")
    permissions_input = input("Set permissions for others (format: user:action;): ")
    
    # Parse permissions
    permissions = {}
    if permissions_input.strip():
        for entry in permissions_input.split(';'):
            if entry.strip():
                user, action = entry.split(':')
                permissions[user.strip()] = [action.strip()]
    
    files[filename] = {"owner": owner, "permissions": permissions}
    print(f"File '{filename}' created with permissions: {permissions}")

# Function to check file access
def access_file(user):
    filename = input("Enter filename to access: ")
    action = input("Enter action (read/write/delete): ").lower()
    
    if filename not in files:
        print("X Error: File does not exist.")
        return
    
    file = files[filename]
    if user == file["owner"]:
        print(f"Access Granted: {user} (owner) can {action} '{filename}'")
    elif user in file["permissions"] and action in file["permissions"][user]:
        print(f"Access Granted: {user} can {action} '{filename}'")
    else:
        print(f"X Access Denied: {user} does not have permission to {action} '{filename}'")

# Main program
print("DAC Scenario: Simple File System")
current_user = input("Enter your username: ")

# Owner creates a file
print(f"\n{current_user}, create a new file:")
create_file(current_user)

# Simulate access attempts
print("\n--- Access Attempts ---")
access_user = input("\nEnter username for access test: ")
access_file(access_user)