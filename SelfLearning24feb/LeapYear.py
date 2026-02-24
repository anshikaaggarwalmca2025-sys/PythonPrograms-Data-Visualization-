#program to check wheater a year is a leap year or not
year = int(input("Enter a year: "))
#checking if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")



output:
Enter a year: 2020  
2020 is a leap year.
Enter a year: 1900
1900 is not a leap year.
Enter a year: 2000
2000 is a leap year.