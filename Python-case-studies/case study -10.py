password = input("Enter a sample password: ")
errors = []

if len(password) < 8:
    errors.append("Use at least 8 characters.")
if not any(ch.isupper() for ch in password):
    errors.append("Include at least one uppercase letter.")
if not any(ch.islower() for ch in password):
    errors.append("Include at least one lowercase letter.")
if not any(ch.isdigit() for ch in password):
    errors.append("Include at least one digit.")
if not any(ch in "!@#$%" for ch in password):
    errors.append("Include at least one special character from !@#$%.")
if "password" in password.lower():
    errors.append("Do not include the word 'password'.")

if len(errors) == 0:
    print("Password meets all classroom policy rules.")
else:
    print("Password does not meet the policy:")
    for error in errors:
        print("-", error)
