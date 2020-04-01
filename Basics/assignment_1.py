"""Write a program that accepts a date in the form month/day/year and outputs
whether or not the date is valid. For example 5/24/1962 is valid, but 9/31/2000 is
not. (September has only 30 days.)"""

date = input("Enter date in the form month/day/year")
month_with_30days = [9, 4, 6, 11]
try:
    # Split the entered date and convert it to string
    date_S = date.split("/")
    splitted_date = ([int(s) for s in date_S])
    validity=True
    # Condition 1, if the date is beyond 31 or the month is beyond 12
    if splitted_date[1] > 31 or splitted_date[0] > 12:
        print("The date is invalid")
        validity = False
    # Condition 2, if the number of days in the months with 30 days is more than 30
    if (splitted_date[0] in month_with_30days)  and  splitted_date[1] > 30:
        print("Error with the month, day number invalid")
        validity = False
    if (validity != False):
        print("The date is valid")

except:
    print("Date is Invalid")

