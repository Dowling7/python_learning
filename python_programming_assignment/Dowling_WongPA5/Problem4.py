# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #5
#
# Description:Write a program that prompts the user for two people’s birthday (month and day), along with
# today’s month and day. The program should figure out how many days remain until each user’s
# birthday and which birthday is sooner with the results displayed on the console. Ignore leap years.
import math
def main():
    date()

def date():
    print("Date input sample--Feb 22, Mar 13")#To tell user how to input date
    month1 = input("Please input the month of person A's birthday")
    day1 = input("Please input the day of person A's birthday")
    day1 = int(day1)
    sum1 = cal(month1, day1)#We convert each date into a integer to calculate their difference
    month2 = input("Please input the month of persona B's birthday")
    day2 = input("Please input the day of person B's birthday")
    day2 = int(day2)
    sum2 = cal(month2, day2)
    month3 = input("Please input current month.")
    day3 = input("Please input current day.")
    day3 = int(day3)
    sum3 = cal(month3, day3)
    if sum1 < sum3:#In case their birthday is passed for this year
        sum1 = 365 + sum1
    else:
        sum1 = sum1
    if sum2 < sum3:
        sum2 = 365 + sum2
    else:
        sum2 = sum2
    interval_1 = abs(sum1 - sum3)
    interval_2 = abs(sum2 - sum3)
    print("Person A's birthday is", interval_1, "days left")
    print("Person B's birthday is", interval_2, "days left")
    if interval_1 > interval_2:
        print("Person A's birthday is sooner!")
    if interval_1 < interval_2:
        print("Person B's birthday is sooner!")
    if interval_1 == interval_2:
        print("Nobody's birthday is sooner, they have the same date of birthday!")

def cal(x, y):
    if x == "Jan":
        z = 0
    if x == "Feb":
        z = 31
    if x == "Mar":
        z = 59
    if x == "Apr":
        z = 90
    if x == "May":
        z = 120
    if x == "Jun":
        z = 151
    if x == "Jul":
        z = 181
    if x == "Aug":
        z = 212
    if x == "Sep":
        z = 243
    if x == "Oct":
        z = 273
    if x == "Nov":
        z = 304
    if x == "Dec":
        z = 335
    z = z + y
    return z

main()

