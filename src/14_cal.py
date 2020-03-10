"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime
# Write a program that accepts user input of the form
# `14_cal.py [month] [year]`


def invalid_month():
    print("Not a valid month please enter a month using the MM format")


def invalid_format():
    print("Invalid Format. Please use the MM YYYY format")


def invalid_year():
    print("Invalid year format. Please use the YYYY format")


if len(sys.argv) == 2 or len(sys.argv) == 3:
    month = int(sys.argv[1])
else:
    month = int(datetime.today().month)

if len(sys.argv) == 3:
    year = int(sys.argv[2])
else:
    year = int(datetime.today().year)

arg_list = [month, year]
print(arg_list)

# If the user doesn't specify any input, your program should print the calendar for the current month.
# if not arg_list[0]:
#     month = datetime.today().month
#     print(calendar.month(2020, month))
# #  If the user specifies one argument, assume they passed in a
# #  month and render the calendar for that month of the current year.
# elif len(arg_list) == 1:
#   print(calender.month(2020, month))
# #  If the user specifies two arguments, assume they passed in
# #  both the month and the year. Render the calendar for that
# #  month and year.
# elif len(arg_list) == 2:
#     if month > 12 or month < 1:
#         invalid_month()
#     elif len(str(year)) < 4:
#         invalid_year()
#     else:
#         print(calendar.month(year, month))
# else:
#     invalid_format()

# refactored
# If the user doesn't specify any input, your program should print the calendar for the current month.
if len(sys.argv) == 1:
    # month = datetime.today().month
    print(calendar.month(year, month))
#  If the user specifies one argument, assume they passed in a
#  month and render the calendar for that month of the current year.
elif len(sys.argv) == 2:
  if len(sys.argv[1]) > 2 or int(sys.argv[1]) > 12 or int(sys.argv[1]) < 1:
    invalid_month()
  else:
    print(calendar.month(year, month))
#  If the user specifies two arguments, assume they passed in
#  both the month and the year. Render the calendar for that
#  month and year.
elif len(sys.argv) == 3:
    if month > 12 or month < 1:
        invalid_month()
    elif len(str(year)) < 4:
        invalid_year()
    else:
        print(calendar.month(year, month))
else:
    invalid_format()
