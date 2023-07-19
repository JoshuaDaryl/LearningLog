def add_time(start, duration, day=None):
    # Splitting 'start' argument and converting to INT, also calculating time based on PM or AM
    startReplacer = start.replace(' ', ':')
    newStart = startReplacer.split(":")
    startHour = int(newStart[0])
    if newStart[2] == "PM":
        startHour = startHour + 12
    startMinutes = int(newStart[1])

    convertedStart = (startHour * 60) + (startMinutes)

    # Splitting 'duration' and converting to INT
    durationReplacer = duration.split(":")
    durationHour = int(durationReplacer[0])
    durationMinutes = int(durationReplacer[1])
    convertedDuration = (durationHour * 60) + durationMinutes

    # Calculating updated time delta
    total_minutes = convertedStart + convertedDuration
    ammendDays, ammendMinutes = divmod(total_minutes, 1440) 
    ammendHours, ammendMinutes = divmod(ammendMinutes, 60)

    if ammendHours >= 12:
        stamp = "PM"
    else:
        stamp = "AM"

    if ammendHours >= 12:
        ammendHours -= 12

    # Handling midnight (12 AM)
    if ammendHours == 0:
        ammendHours = 12

    newHours = str(ammendHours)

    # Using string formatting to ensure minutes are displayed with a leading zero when necessary
    newMins = "{:02d}".format(ammendMinutes)

    new_time = newHours + ":" + newMins + " " + stamp

    # Handling the day
    if day is not None:
        dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        newDay = day.title()
        if newDay in dayList:
            index = (dayList.index(newDay) + ammendDays) % 7
            new_time += f", {dayList[index]}"

    # Handling days later
    if ammendDays == 1:
        new_time += " (next day)"
    elif ammendDays > 1:
        new_time += f" ({ammendDays} days later)"

    return new_time
