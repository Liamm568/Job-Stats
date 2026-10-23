from difflib import get_close_matches


User_Hours = 0
Set_Pay_Rate = 0
Calculate_Overtime = 0

menu_options = {
    "add hours": "Add Hours",
    "set pay rate": "Set Pay Rate",
    "calculate total pay": "Calculate Total Pay",
    "calculate overtime": "Calculate Overtime",
    "exit": "Exit",
}


def get_menu_choice():
    menu = "Hello, what would you like to do?:\n" + "\n".join(menu_options.values())
    choice = input(menu + "\n")
    normalized_choice = choice.strip().lower()

    if normalized_choice in menu_options:
        return menu_options[normalized_choice]

    close_match = get_close_matches(normalized_choice, menu_options, n=1, cutoff=0.6)
    if close_match:
        print(f"Using '{menu_options[close_match[0]]}'.")
        return menu_options[close_match[0]]

    print("I did not understand that choice. Please try again.")
    return None


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
                file.write(f"User_Hours: {User_Hours}\n")
                break
            except ValueError:
                print("Please enter a valid, non-negative number of hours.")

    elif user_choice == "Set Pay Rate":
        while True:
            try:
                Set_Pay_Rate = float(input("Enter your pay rate: "))
                if Set_Pay_Rate < 0:
                    raise ValueError
                file.write(f"Set_Pay_Rate: {Set_Pay_Rate}\n")
                break
            except ValueError:
                print("Please enter a valid, non-negative pay rate.")

    elif user_choice == "Calculate Total Pay":
        Calculate_Total_Pay = round(User_Hours * Set_Pay_Rate, 2)
        print("Your total pay is: $",Calculate_Total_Pay)

    elif user_choice == "Calculate Overtime":
        if User_Hours > 40:
            overtime_hours = User_Hours - 40
            overtime_pay = overtime_hours * (Set_Pay_Rate * 1.5)
            Calculate_Overtime = round(overtime_pay, 2)
            print("Your overtime pay is: $", Calculate_Overtime)
        else:
            print("You have not worked overtime hours.")



