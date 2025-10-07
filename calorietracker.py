# Name - sakshi Yogi
# Date: 2025-10-07
# Project: Daily Calorie Tracker

print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you log your meals and calories, compare against your daily limit, and save your session.\n")

meal_names = []
calorie_amounts = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals): 
    
    meal = input(f"Enter meal name: ")
    calories = float(input(f"Enter calorie amount: "))
    meal_names.append(meal)
    calorie_amounts.append(calories)

total_calories = sum(calorie_amounts)
average_calories = total_calories / len(calorie_amounts)
daily_limit = float(input("\nEnter your daily calorie limit: "))
if total_calories > daily_limit:
    status_msg = f"Warning: You have exceeded your daily limit by {total_calories - daily_limit} calories."
else:
    status_msg = f"Within the daily limit. You have {daily_limit - total_calories} calories remaining."

print("\n\n--- Daily Calorie Summary ---")
print("Meal Name\tCalories")
print("-" * 30)

for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal}\t\t{cal}")

print(f"Total:\t\t{total_calories:}")
print(f"Average:\t{average_calories:}")
print(status_msg)