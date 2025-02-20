from datetime import datetime

# Dictionary to store file access policies
files = {}

def check_time():
    # Check if current time is during work hours (9 AM to 5 PM)
    now = datetime.now()
    return 9 <= now.hour < 17

def check_device(device_id):
    # Simplified check if the device is company-approved (in practice, this would consult a device registry)
    approved_devices = ["company_device_1", "company_device_2", "company_device_3"]
    return device_id in approved_devices

def access_file(user, device_id, filename):
    if filename not in files:
        print(f"Error: File '{filename}' does not exist.")
        return

    if not check_time():
        print("Access Denied: Outside work hours.")
        return

    if not check_device(device_id):
        print("Access Denied: Device not approved.")
        return

    # If both time and device checks pass, grant access
    print(f"Access Granted: User '{user}' from device '{device_id}' can access '{filename}'.")

# Main program loop
print("ABAC Simulation for Cloud Storage")
user = input("Enter your username: ")
while True:
    command = input("Enter command (access/quit): ").lower()
    if command == 'quit':
        break
    elif command == 'access':
        filename = input("Enter filename to access: ")
        device_id = input("Enter your device ID: ")
        access_file(user, device_id, filename)
    else:
        print("Invalid command. Use 'access' or 'quit'.")