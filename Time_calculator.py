def add_time(start, duration, day = ""):
    """
    add_time function is a function that calculates the resulting time after the duration.
    start: string of the starting time with AM/PM
    duration: string of the duration, to which should be added to the start time
    day: string of the day of the week (optional); default is no day given
    
    Returns: string of the new time
    """

    # Split the start time between the time and AM/PM
    start_time = start.split(" ")[0]
    am_or_pm = start.split(" ")[1]

    # Split the start time into hours and minutes
    start_hrs = int(start_time.split(":")[0])
    start_mins = int(start_time.split(":")[1])

    # Split the duration into hours and minutes
    dur_hrs = int(duration.split(":")[0])
    dur_mins = int(duration.split(":")[1])

    # Add the hours and minutes together
    tot_mins = start_mins + dur_mins
    tot_hrs = start_hrs + dur_hrs

    # This variable will keep track of the number of days
    num_days = 0

    # This variable will keep track of the hours for days calculation
    hor_to_days = 0

    # Keep a list of the days:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # If the number of minutes exceeds 60, then we need to add this to the hours and keep the remainder in mins
    if tot_mins >= 60:
        # To get the hours, we do integer division by 60
        hours = tot_mins // 60
        # To get the mins, we do mod division
        mins = tot_mins % 60

        # Add the new number of hours to total hours
        tot_hrs += hours
        # Replace the total number of numbers by new calculated mins
        tot_mins = mins
    
    if tot_mins < 10:
        str_mins = "0" + str(tot_mins)
        tot_mins = str_mins

    # There are different cases to deal with:
    # If the current time is AM/PM and doesn't become AM/PM; the sum of the hours is not greater than 12
    if tot_hrs < 12:
        new_time = str(tot_hrs) + ":" + str(tot_mins) + " " + am_or_pm

    # If the current time is AM/PM and become AM/PM; the sum of the hours is greater than 12
    elif tot_hrs >= 12:
        pass
        # We have to figure out if the resulting time will be in AM or PM
        # If the number of times the total hours goes into 12 is odd, then it is the opposite (AM -> PM)
        # If it is even, then it is the same (AM -> AM)

        change = tot_hrs // 12

        hor_to_days = tot_hrs

        # If the number of times is odd
        if change % 2 == 1:
            # If the current time is AM, change to PM
            if am_or_pm == "AM":
                am_or_pm = "PM"
            # Else change to AM
            else:
                am_or_pm = "AM"
                # If the time changes from AM -> PM, then it is the next day, so we add 1 day
                num_days += 1
        
        # New hours is calculated
        if tot_hrs % 12 == 0:
            tot_hrs = 12
        else:
            tot_hrs = tot_hrs % 12

        # Set the new time with the new calculated hours, mins, am or pm
        new_time = str(tot_hrs) + ":" + str(tot_mins) + " " + am_or_pm

    # We also need to understand if the day changes and/or if a day is passed in as an argument

    # The day changes if the total number of hours at least exceeds by 24 hours
    # We can figure out the number of days by taking the total hours and doing int division
    num_days += hor_to_days // 24

    # If the day parameter is not given,
    if day == "":
        # If the number of days is 1, then it is the next day
        if num_days == 1:
            new_time += " " + "(next day)"
        # If the number of days is 0, then the day hasn't changed
        elif num_days == 0:
            pass
        # If the number of days is greater than 1, then day add the number of days to new_time
        else:
            new_time += " " + "(" + str(num_days) + " days later)"
    # If the day parameter is given, 
    else:
        # Save the day as a lower-case version
        dow = day.lower()

        # We have to find the index of the day given
        d = [x.lower() for x in days]
        index_of_dow = d.index(dow)

        # If the number of days is 1, then it is the next day
        if num_days == 1:
            # If the given day is the last day of the week, then the next day is the first day of the week
            if index_of_dow == 6:
                new_time += ", " + days[0] + " (next day)"
            # Else the day is not the last day, so we add 1 to the index of dow
            else:
                day_of_week = (index_of_dow + 1) % 7
                new_time += ", " + days[day_of_week] + " (next day)"
        # If the number of days is 0, then the day hasn't changed
        elif num_days == 0:
            new_time += ", " + days[index_of_dow]
        # If the number of days is greater than 1, then day add the number of days to new_time
        else:
            day_of_week = (num_days + index_of_dow) % 7
            new_time += ", " + days[day_of_week] + " (" + str(num_days) + " days later)"

    # Return the new_time to the function call
    return new_time

print(add_time('2:59 AM', '24:00', 'saturDay'))