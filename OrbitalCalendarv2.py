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
    # Clear the calendar dictionary
    calendar.clear()

    # Initialize the Gregorian date to the start of the year
    gregorian_date = datetime.date(year, 1, 1)

    # Create a new calendar for this year
    calendar[year] = {}

    # Fill the calendar
    for month in months:
        calendar[year][month] = {}
        for week in weeks:  # Each month has 4 weeks
            week_days = []
            for day in days:  # Each week has 7 days
                # Add the day to the calendar
                week_days.append(day)
            calendar[year][month][week] = week_days

    # Add Leap Day if it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_day = "Leap Day"
        # Insert Leap Day on the 4th day of the 3rd month, between Fooday and Knoday
        calendar[year]["Month 3"]["Spring Week"].insert(3, leap_day)

    # Add Last Day at the end of the year
    last_day = "Last Day"
    calendar[year]["Month 13"]["Winter Week"].append(last_day)

    # Assign the Gregorian dates
    for month in months:
        for week in weeks:
            for i in range(len(calendar[year][month][week])):
                # Assign the Gregorian date to the day
                day = calendar[year][month][week][i]
                if isinstance(day, tuple):
                    day = day[0]
                calendar[year][month][week][i] = (day, gregorian_date)
                # Increment the Gregorian date
                gregorian_date += datetime.timedelta(days=1)

# Generate the calendar for the current year
generate_calendar(year)

# Get the length of the longest week name
max_week_name_length = max(len(week) for week in weeks)

# Get the length of the longest day name
max_day_name_length = max(len(day) for day in days + ["Leap Day", "Last Day"])

# Print the calendar
print('Year:', year)
for month, weeks in calendar[year].items():
    print(month)
    for week, days in weeks.items():
        # Use the length of the longest week name to align the ':'
        print('  ', week.ljust(max_week_name_length) + ':', end=' ')
        # Pad the day names to the length of the longest day name
        print(' | '.join(f"{day[0]} ({day[1].month}/{day[1].day})".ljust(max_day_name_length + 6) for day in days))
    print()

# Ask the user to quit
input("Press any key to quit.")