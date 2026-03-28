import re

print("=== Password Strength Checker ===")

password = input("Enter your password: ")

strength = 0

# Check length
if len(password) >= 8:
    strength += 1

# Check uppercase letter
if re.search("[A-Z]", password):
    strength += 1

# Check number
if re.search("[0-9]", password):
    strength += 1

# Check special character
if re.search("[@#$%^&*!]", password):
    strength += 1

# Show result
if strength <= 1:
    print("Password Strength: Weak ❌")

elif strength == 2 or strength == 3:
    print("Password Strength: Medium ⚠️")

else:
    print("Password Strength: Strong ✅")