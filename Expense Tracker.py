budget = int(input("Enter your budget: "))
food_expenses = int(input("Enter your food expenses: "))
Transport_expenses = int(input("Enter your transport expenses: "))
Other_expenses = int(input("Enter your other expenses: "))
Total_expediture = food_expenses + Transport_expenses + Other_expenses
Remaining_budget = budget - Total_expediture
print("Total expenses:", Total_expediture)
print("Remaining budget:", Remaining_budget)
if Total_expediture > budget:
    print("You have exceeded your budget.")
elif Total_expediture < budget:
    print("You are within your budget.")
else:
    print("You have exactly met your budget.")
input("Press Enter to exit...")
