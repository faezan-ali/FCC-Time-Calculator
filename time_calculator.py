def add_time(start, duration, day=False):
#split input and create variables
    parts = start.split()
    timesplit = parts[0].split(":")
    startampm = parts[1]
    starthrs = int(timesplit[0])
    startmins = int(timesplit[1])
    dursplit = duration.split(":")
    addhrs = int(dursplit[0])
    addmins = int(dursplit[1])
    weekday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#calculate resulting minutes
    endmins = (startmins + addmins)%60
    if endmins <10:
        endmins = str(endmins).zfill(2)
    newhr = (startmins+ addmins)//60
#calculate resulting hours
    endhr = (starthrs + addhrs + newhr)%12
    if endhr == 0:
        endhr = 12
    halfdaycycle = (starthrs + addhrs + newhr)//12
# function to calculate and return no. of days passed
    def xdayslater(dayscounter):
        if num_of_days == 1:
            days = "next day"
            return days
        elif num_of_days >= 1:
            days = str(num_of_days) + " days later"
            return days
        elif num_of_days == 0:
            days = 0
            return days
# function to determine day of week
    def dayofweek(dayindex, count):
        if count > 6:
            addays = count%7
        else:
            addays = count
        dayindex = dayindex + addays
        if dayindex > 6:
            dayindex = dayindex - 7
        return dayindex
# check if day input recieved
    if day:
        dayindex = weekday.index(day.lower())
        count = 0
    else:
        pass
#calculate no of days passed, if only full days
    if halfdaycycle%2 == 0:
        num_of_days = halfdaycycle//2
        days = xdayslater(num_of_days)
        count = num_of_days
#calculate day of week
        if day:
            dayindex = dayofweek(dayindex, count)
            day = weekday[dayindex]

#calculate no of days passed, if not full days
    else:
        if startampm == "AM":
            num_of_days = halfdaycycle//2
            days = xdayslater(num_of_days)
        elif startampm == "PM":
            num_of_days = (halfdaycycle//2)+1
            days = xdayslater(num_of_days)
        count = num_of_days
        if day:
            dayindex = dayofweek(dayindex, count)
            day = weekday[dayindex]

#calculate if AM or PM
    if halfdaycycle == 0:
        ampm = startampm
    elif halfdaycycle%2 == 0:
        ampm = startampm
    elif halfdaycycle%2 != 0:
        if startampm == "AM":
            ampm = "PM"
        if startampm == "PM":
            ampm = "AM"

# return time outputs
    if bool(day) and days!= 0:
        new_time = str(endhr) + ":" + str(endmins) + " " + str(ampm) +", "+ day.capitalize()+" " + "("+days+")"
    elif bool(day) and days == 0:
        new_time = str(endhr) +  ":"+ str(endmins) + " " + ampm +", "+ day.capitalize()
    elif days == 0:
        new_time = str(endhr) +  ":"+ str(endmins) + " " + ampm
    else:
        new_time = str(endhr) +  ":"+ str(endmins) + " " + ampm + " " + "("+ days+")"

    return new_time
