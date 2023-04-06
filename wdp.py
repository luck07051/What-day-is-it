import random
import datetime
import time
from colorama import Fore, Style
import sys, tty, termios
import argparse


def random_day(y_start, y_end):
    start_dt = datetime.date(y_start, 1, 1)
    end_dt = datetime.date(y_end, 12, 31)
    days_between_dates = (end_dt - start_dt).days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_dt + datetime.timedelta(days=random_number_of_days)
    return random_date


def show_doomsday_how(day):
    pass


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", "-s", metavar='N', type=int, default=2000, help="start year")
    parser.add_argument("--end", "-e", metavar='N', type=int, default=2100, help="end year")
    parser.add_argument("--notime", action='store_true', help="dont print time")
    arg = parser.parse_args()

    # Init key input
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    # Init log value
    log_time = []
    log_cor = 0
    log_incor = 0
    log_noans = 0

    while True:
        day = random_day(arg.start, arg.end)
        print(day)

        # Reset value
        is_correct = None
        s_clock = time.time()

        # Key event
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if key == "q":
            break
        if key in "01234567":
            if int(key)%7 == day.isoweekday():
                is_correct = True
            else:
                is_correct = False

        # Compute time
        using_time = time.time() - s_clock
        log_time.append(using_time)

        # Print answer
        print("\t->", day.isoweekday()%7, day.strftime("%A"))

        # Print using time
        if not arg.notime:
            print("\ttime:", "%.2f" % using_time + 's')

        # Print correct or not
        if is_correct is None:
            log_noans += 1
        elif is_correct:
            print(Fore.GREEN + "\tCorrect!" + Style.RESET_ALL)
            log_cor += 1
        elif not is_correct:
            print(Fore.RED + "\tIncorrect!" + Style.RESET_ALL)
            log_incor += 1


    print("\n")
    if not arg.notime:
        print("Average time:", "%.2f"%(sum(log_time)/len(log_time)))
    print("Total:", log_noans + log_cor + log_incor)
    print("Correct:", log_cor)
    print("Incorrect:", log_incor)
    print("Correct/Incorrect:", "%.2f"%(log_cor/log_incor))


if __name__ == '__main__':
    __main__()
