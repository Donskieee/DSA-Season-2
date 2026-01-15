import calendar
from datetime import datetime

# Initialize sample data
birthdays = {
    11: "Ivan",
    14: "Jems"
}

def display_calendar(year, month):
    # For display calendar
    print(f"\n      {calendar.month_name[month]} {year}")
    print("Mon Tue Wed Thu Fri Sat Sun")
    
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        line = ""
        for day in week:
            if day == 0:
                line += "    "
            elif day in birthdays:
                # Highlighting birthdays
                line += f"[{day:2}]" 
            else:
                line += f" {day:2} "
        print(line)

def main_menu():
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month

    while True:
        # 1. Header & Calendar View
        print("\n" + "="*30)
        print("   YAGBALLS BIRTHDAY TRACKER")
        print("         DSA Project")
        print("="*30)
        
        display_calendar(year, month)
        
        print(f"\n Birthdays in {calendar.month_name[month]}:")
        for day, name in birthdays.items():
            print(f" - {day}: {name}")

        # 2. Menu Options from your image
        print("\n--- MENU ---")
        print("1. Add Birthday")
        print("2. Search Birthday")
        print("3. Delete Birthday")
        print("4. Enable Persistent Reminders (Set Time)")
        print("5. Disable Persistent Reminders (Turn Off)")
        print("6. Next Month / Prev Month")
        print("7. Exit")
        
        choice = input("Select: ")

        if choice == '1':
            # Logic for adding a birthday
            pass
        elif choice == '2':
            # Logic for searching
            pass
        elif choice == '3':
            # Logic for deleting
            pass
        elif choice == '6':
            # Logic to toggle months
            month = month + 1 if month < 12 else 1
        elif choice == '7':
            print("Exiting tracker...")
            break
        else:
            print("Feature coming soon or invalid input!")

if __name__ == "__main__":
    main_menu()
