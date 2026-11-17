from datetime import datetime

ETitle = input("Enter The Event Title: ")
Year = int(input("Year: "))
Month = int(input("Enter Month (number): "))
Day = int(input("Day: "))

event_date = datetime(Year, Month, Day)

print("\nFormatted Output:")
print(f"Event: {ETitle.upper()}")
print(f"Date: {event_date.strftime('%B %d, %Y')}")
print(f"Year: {Year}")
print(f"Month: {event_date.strftime('%B')}")
print(f"Day: {Day}")
print(f"Weekday: {event_date.strftime('%A')}")