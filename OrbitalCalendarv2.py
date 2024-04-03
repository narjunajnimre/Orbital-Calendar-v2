import datetime

# Define the names of the months, weeks, and the days of the week
months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6", "Month 7", "Month 8", "Month 9", "Month 10", "Month 11", "Month 12", "Month 13"]
weeks = ["Spring Week", "Summer Week", "Fall Week", "Winter Week"]
days = ["Chorday", "Devday", "Fooday", "Knoday", "Wilday", "Artday", "Sabbath"]

# Create the calendar
calendar = {}

# Define the year
year = datetime.datetime.now().year

def generate_calendar(year):
    # Create a new calendar for this year
    calendar[year] = {}

    # Fill the calendar
    for month in months:
        calendar[year][month] = {}
        for week in weeks:  # Each month has 4 weeks
            week_days = []
            for day in days:  # Each week has 7 days
                week_days.append(day)
            calendar[year][month][week] = week_days

    # Add the Last Day as the 8th day of the 4th week of the 13th month
    calendar[year]["Month 13"]["Winter Week"].append("Last Day")

    # Add Leap Day if it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_day = "Leap Day"
        # Insert Leap Day on the 4th day of the 3rd month, between Fooday and Knoday
        calendar[year]["Month 3"]["Spring Week"].insert(3, leap_day)

# Generate the calendar for the current year
generate_calendar(year)

# Get the length of the longest week name
max_week_name_length = max(len(week) for week in weeks)

# Get the length of the longest day name
max_day_name_length = max(len(day) for day in days + ["Leap Day", "Last Day"])

# Print the calendar
while True:
    current_year = year
    print('Year:', current_year)
    for month, weeks in calendar[current_year].items():
        print(month)
        for week, days in weeks.items():
            # Use the length of the longest week name to align the ':'
            print('  ', week.ljust(max_week_name_length) + ':', end=' ')
            # Pad the day names to the length of the longest day name
            print(' | '.join(day.ljust(max_day_name_length) for day in days))
        print()

    # Ask the user if they want to continue
    user_input = input("Press 'n' to advance to the next year, 'p' to go to the previous year, 's' to go to a specified year or 'q' to quit: ")
    if user_input.lower() == 'q':
        break
    elif user_input.lower() == 'n':
        year += 1
    elif user_input.lower() == 'p':
        year -= 1
    elif user_input.lower() == 's':
        specified_year = int(input("Enter a year between 0000 and 5000: "))
        if 0 <= specified_year <= 5000:
            year = specified_year
        else:
            print("Invalid year. Please enter a year between 0000 and 5000.")
            continue

    # Generate the calendar for the year if it doesn't exist
    if year not in calendar:
        generate_calendar(year)