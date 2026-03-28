import re

print("=================================")
print("   Password Strength Checker 🔐  ")
print("=================================")

password = input("Enter your password: ")

score = 0
feedback = []

# Check length
if len(password) >= 8:
    score += 1
else:
    feedback.append("Password should be at least 8 characters long.")

# Check uppercase
if re.search("[A-Z]", password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

# Check lowercase
if re.search("[a-z]", password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

# Check numbers
if re.search("[0-9]", password):
    score += 1
else:
    feedback.append("Include at least one number.")

# Check special characters
if re.search("[@#$%^&*!]", password):
    score += 1
else:
    feedback.append("Include at least one special character (@#$%^&*!).")

# Display score
print("\nPassword Score:", score, "/ 5")

# Strength result
if score <= 2:
    print("Password Strength: Weak ❌")

elif score == 3 or score == 4:
    print("Password Strength: Medium ⚠️")

else:
    print("Password Strength: Strong ✅")

# Show feedback
if feedback:
    print("\nSuggestions to improve your password:")
    for item in feedback:
        print("-", item)
else:
    print("\nGreat job! Your password looks secure.")
