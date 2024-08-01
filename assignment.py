# Step 0: 
# Programmer: [Darcy Ostrander]
# Course: CS701/GB-731, Dr. Yalew
# Date: [8/6/2024]
# Programming Assignment: 2
# Program Inputs: Month (as a number in the range 1 through 12), Year
# Program Outputs: Number of days in the given month

def main():

    # Step 1: Ask the user for the month and year
    month = int(input("Please enter the month as a number between 1 through 12: "))
    year = int(input("Please enter the year: "))

    # Step 2: Determine if the year is a leap year
    if year % 100 == 0:
        isLeapYear = year % 400 == 0
    else:
        isLeapYear = year % 4 == 0
    # Step 3: Determine the number of days in the month
    days = 0
    if month == 1:
        days = 31
    elif month == 2:
        if isLeapYear:
            days = 29
        else:
            days = 28
    elif month == 3:
        days = 31
    elif month == 4:
        days = 30
    elif month == 5:
        days = 31
    elif month == 6:
        days = 30
    elif month == 7:
        days = 31
    elif month == 8:
        days = 31
    elif month == 9:
        days = 30
    elif month == 10:
        days = 31
    elif month == 11:
        days = 30
    elif month == 12:
        days = 31
    else:
        print ("Invalid month")

    # Step 4: Output the number of days in the month
    print("The month has " + str(days) +" days")
   
if __name__ == "__main__":
    main()