# RBAC Scenario: Hospital Information System

# Define roles and their permissions
roles = {
    "doctor": ["view_patient_record", "edit_patient_record"],
    "administrative_staff": ["manage_appointments", "update_patient_info"],
    "nurse": ["view_patient_record"]
}

# User roles dictionary
user_roles = {
    "Dr.Smith": "doctor",
    "JaneDoe": "administrative_staff",
    "NurseJones": "nurse"
}

def check_permission(user, action):
    # Check if the user exists and has a role
    if user not in user_roles:
        return "User not found in the system."
    
    user_role = user_roles[user]
    if user_role not in roles:
        return "Role not defined for this user."

    # Check if the action is permitted for the user's role
    if action in roles[user_role]:
        return f"Access Granted: {user} can {action}."
    else:
        return f"Access Denied: {user} cannot {action}."

# Interactive user attempts
print("RBAC Scenario: Hospital Information System")

while True:
    user = input("Enter username (or 'quit' to exit): ")
    if user.lower() == 'quit':
        break
    
    if user not in user_roles:
        print("User not found in the system. Please try again.")
        continue

    action = input(f"Enter action for {user} (view_patient_record/edit_patient_record/manage_appointments/update_patient_info): ")
    print(check_permission(user, action))