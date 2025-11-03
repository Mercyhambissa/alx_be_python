from datetime import datetime, date, time, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}"

future_variable = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    today = datetime.now().date()
    days_to_add = timedelta(days = future_variable)
    future_date = today + days_to_add
    return f"Future date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}"
