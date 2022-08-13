# What Day is it Practice Script

import random
import datetime
import sys, tty, termios


def random_day(y_start, y_end):
    start_dt = datetime.date(y_start, 1, 1)
    end_dt = datetime.date(y_end, 12, 31)
    days_between_dates = (end_dt - start_dt).days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_dt + datetime.timedelta(days=random_number_of_days)
    return random_date

# Init key input
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

# Default value
y_start = 2000
y_end = 2100

if len(sys.argv) > 1:
    y_start = int(sys.argv[1])
if len(sys.argv) > 2:
    y_end = int(sys.argv[2])

while True:
    day = random_day(y_start, y_end)
    print(day)

    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    match ch:
        case "q":
            break

    print(" ->", day.isoweekday()%7, day.strftime("%A"))
