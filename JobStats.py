# Job Stats Program 
import questionary
from difflib import get_close_matches
from pathlib import Path
print("Welcome to the Job Stats Program!")
User_Hours = 0
Set_Pay_Rate = 0
Calculate_Overtime = 0
hours_file = Path("WorkHours.txt")
pay_rate_file = Path("PayRate.txt")
week_num = 0

# Checks if the file exists and counts the number of weeks recorded in the file
if hours_file.is_file():
    with hours_file.open("r", encoding="utf-8") as file:
        week_num = sum(1 for _ in file)

# Uses function to get user input and return the corresponding menu option, or None if the input is invalid
def get_menu_choice():
    return questionary.select(
        "What would you like to do?",
        choices=[
            "Add Hours",
            "Manage Pay Rate",
            "See Hours",
            "Calculate Total Pay",
            "Calculate Overtime",
            "Load Saved Data",
            "Save Data",
            "Exit"
        ]
    ).ask()


# Main loop to display the menu and handle user choices
while True:
    user_choice = get_menu_choice()

    if user_choice == "Exit":
        print("Exiting the program. Goodbye!")
        break

    if user_choice == "Add Hours":
        while True:
            try:
                User_Hours = float(input("Enter the number of hours worked: "))
                if User_Hours < 0:
                    raise ValueError
                next_week_num = week_num + 1
                with hours_file.open("a", encoding="utf-8") as file:
                    file.write(f"Week {next_week_num}: {User_Hours} hours\n")
                week_num = next_week_num
                break
            except ValueError:
                print("Please enter a valid, non-negative number of hours.")

    if user_choice == "Manage Pay Rate":
        while True:
            try:
                pay_rate_choice = questionary.select(
                    "What would you like to do?",
                    choices=[
                        "Set Pay Rate",
                        "Change Pay Rate"
                    ]
                ).ask()

                if pay_rate_choice is None:
                    break
                elif pay_rate_choice == "Set Pay Rate":
                    Set_Pay_Rate = float(input("Enter your pay rate: "))
                    if Set_Pay_Rate < 0:
                        raise ValueError
                    with pay_rate_file.open("w", encoding="utf-8") as file:
                        file.write(f"Pay Rate: {Set_Pay_Rate}\n")
                    break
                elif pay_rate_choice == "Change Pay Rate":
                    Set_Pay_Rate = float(input("Enter the new pay rate: "))
                    if Set_Pay_Rate < 0:
                        raise ValueError
                    with pay_rate_file.open('r+', encoding="utf-8") as f:
                        content = f.read()
                        anchor = content.index('Pay Rate:')
                        pos = anchor + len('Pay Rate:')

                        while content[pos] in ' :':
                            pos += 1

                        # find where old value ends
                        end = pos
                        while end < len(content) and content[end] not in '\n ':
                            end += 1

                        content = content[:pos] + str(Set_Pay_Rate) + content[end:]
                        f.seek(0)
                        f.truncate()
                        f.write(content)

                    with hours_file.open("r", encoding="utf-8") as file:
                        print(file.read())
                    break
            except ValueError:
                print("Please enter a valid, non-negative pay rate.")

    if user_choice == "Change Hours":
        while True:
            try:
                week = int(input("What week do you want to change? "))
                if week <= 0:
                    raise ValueError
                User_Hours = float(input("Enter the new number of hours worked: "))
                with hours_file.open('r+', encoding="utf-8") as f:
                    content = f.read()

                    anchor = content.index(f'Week: {week}')
                    pos = anchor + len(f'Week: {week}')

                    while content[pos] in ' :':
                        pos += 1

                    # find where old value ends
                    end = pos
                    while end < len(content) and content[end] not in '\n ':
                        end += 1

                    content = content[:pos] + str(User_Hours) + content[end:]
                    f.seek(0)
                    f.truncate()
                    f.write(content)

                    with hours_file.open("r", encoding="utf-8") as file:
                            print(file.read())
                            break
            except ValueError:
                print("Please enter a valid week number and non-negative hours.")


    if user_choice == "See Hours":
        with hours_file.open("r", encoding="utf-8") as file:
            if hours_file.is_file():
                print(file.read())
            else:
                print("No work hours data found.")

    if user_choice == "Calculate Total Pay":
        Calculate_Total_Pay = round(User_Hours * Set_Pay_Rate, 2)
        print("Your total pay is: $",Calculate_Total_Pay)

    if user_choice == "Calculate Overtime":
        if User_Hours > 40:
            overtime_hours = User_Hours - 40
            overtime_pay = overtime_hours * (Set_Pay_Rate * 1.5)
            Calculate_Overtime = round(overtime_pay, 2)
            print("Your overtime pay is: $", Calculate_Overtime)
        else:
            print("You have not worked overtime hours.")

    if user_choice == "Load Saved Data":
        if hours_file.is_file():
            with hours_file.open("r", encoding="utf-8") as file:
                print("Loaded Work Hours:")
                print(file.read())
        else:
            print("No saved work hours data found.")

        if pay_rate_file.is_file():
            with pay_rate_file.open("r", encoding="utf-8") as file:
                print("Loaded Pay Rate:")
                print(file.read())
        else:
            print("No saved pay rate data found.")

    if user_choice == "Save Data":
        with hours_file.open("r", encoding="utf-8") as file:
            print("Saved Work Hours:")
            print(file.read())

        with pay_rate_file.open("r", encoding="utf-8") as file:
            print("Saved Pay Rate:")
            print(file.read())
