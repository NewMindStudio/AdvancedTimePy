def get_day_of_week_new(month, day, year):
    #Days
    days = { 0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday" }

    #Month codes
    month_codes = { 1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5 }

    #Fix for leap years, as only January and February have a different code
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 1:
            month = 4
        elif month == 2:
            month = 8

	#Returns the day of the week based on : Day + Month (Code) + Year (Last two digits) + Year (Last two digits) / 4 + Century
    return days[(day + month_codes[month] + year % 100 + (year % 100) // 4 + 6 - 2 * ((year // 100) % 4)) % 7];