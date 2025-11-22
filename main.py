print("===== Personalized Health Risk Checker =====")

age = int(input("Enter your age: "))
bp = int(input("Enter your blood pressure (systolic): "))
sugar = int(input("Enter your fasting sugar level (mg/dL): "))

print("\nLifestyle options:")
print("1. Active")
print("2. Moderate")
print("3. Sedentary")

choice = int(input("Choose your lifestyle (1/2/3): "))

if choice == 1:
    lifestyle = "Active"
elif choice == 2:
    lifestyle = "Moderate"
else:
    lifestyle = "Sedentary"

# --- Risk Checking Logic ---
risk = ""

if age > 55 or bp > 140 or sugar > 125:
    if lifestyle == "Sedentary":
        risk = "High Health Risk"
    else:
        risk = "Moderate Health Risk"

elif 35 <= age <= 55:
    if bp > 130 or sugar > 110:
        risk = "Moderate Health Risk"
    else:
        risk = "Low Health Risk"

else:
    if bp > 130 or sugar > 110:
        risk = "Moderate Health Risk"
    else:
        risk = "Low Health Risk"

print("\n===== RESULT =====")
print(f"Age: {age}")
print(f"Blood Pressure: {bp}")
print(f"Fasting Sugar Level: {sugar} mg/dL")
print(f"Lifestyle: {lifestyle}")
print("\nFinal Assessment:", risk)
