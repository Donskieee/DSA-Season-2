#utils.py

def is_valid_date(date_str):
    
    #checks if string yung input
    if not isinstance(date_str, str):
        return False
    
    #if string si input it get split in the "-" part
    parts = date_str.split("-")
    if len(parts) != 2:
        return False
    
    month_str, day_str = parts



    #checks if month and day string are digits
    if not month_str.isdigit() or not day_str.isdigit():
        return False

    #converts month and day from string to integers
    month = int(month_str)
    day = int(day_str)

    if month  > 12 or month < 1:
        return False
    
    #also works for leap years

    days_in_month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,

    }
    #checks if day is less than 1 or more than day_in_month
    if day < 1 or day > days_in_month[month]:
        return False
    
    return True
