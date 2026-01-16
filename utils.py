# utils.py

def is_valid_date(date_str):
    
    # Check basic format
    if not isinstance(date_str, str):
        return False

    parts = date_str.split("-")
    if len(parts) != 2:
        return False

    month_str, day_str = parts

    # Check if both parts are numeric
    if not month_str.isdigit() or not day_str.isdigit():
        return False

    month = int(month_str)
    day = int(day_str)

    
    if month < 1 or month > 12:
        return False

    #non leap year
    days_in_month = {
        1: 31,  
        2: 28,  
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    
    if day < 1 or day > days_in_month[month]:
        return False


    return True

