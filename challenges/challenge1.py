# Converting 12-hour time to 24-hour timeConverting 12-hour time to 24-hour time
def convert_to_24hr():
    # Prompt user for input
    hour = int(input("Enter the hour(1 to 12): "))
    minute = int(input("Enter the minute(0 to 59): "))
    period = input("Enter 'am' or 'pm': ").lower()

    if period == 'am' and hour == 12:
        #Midnight
        hour == 0
    elif period == 'pm' and hour != 12:
        #Midday
        hour += 12   

    #Format the result as a four-digit string
    result = f"{hour:02d}{minute:02d}"  
    return result  