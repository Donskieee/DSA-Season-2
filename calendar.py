import calendar
from data_storage import storage  # Importing your existing storage instance

def show_monthly_calendar(year, month):
    """
    Displays a visual calendar and lists birthdays for the specific month
    by querying the Hash Table.
    """
    
    # 1. Print the standard visual calendar grid
    print(f"\n{'='*10} CALENDAR VIEW {'='*10}")
    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal.prmonth(year, month)
    print("=" * 35)

    # 2. Iterate through every day of this month to find birthdays
    print(f"Birthdays in {calendar.month_name[month]}:")
    
    # monthrange returns (weekday_of_first_day, number_of_days)
    _, num_days = calendar.monthrange(year, month)
    
    found_birthday = False

    for day in range(1, num_days + 1):
        # Construct the Key to match your data format (e.g., "1-15" or "12-25")
        # Ensure this matches how you input data in main.py
        date_key = f"{month}-{day}"

        # Query your existing Hash Table
        names = storage.search_by_date(date_key)
        
        if names:
            # names is a list, so we join them nicely
            names_string = ", ".join(names)
            print(f"  [ Day {day} ] : {names_string}")
            found_birthday = True

    if not found_birthday:
        print("  (No birthdays found for this month)")
    
    print("=" * 35 + "\n")