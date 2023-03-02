from datetime import date, timedelta


# Task 10

def subtract_days_from_today(days_to_subtract):
    today = date.today()
    old_date = today - timedelta(days=days_to_subtract)
    print(f"Current date: {today}")
    print(f"Counted date: {old_date}")
    return old_date

subtract_days_from_today(5)
