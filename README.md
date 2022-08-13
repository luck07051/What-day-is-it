# What Day is it Practice Script

Simple script to practice 'day of week calculate skill'. I wrote this script for practice The Doomsday Algorithm that I find in [this video](https://youtu.be/z2x3SSBVGJU).

## How to use

Run the script:
```
python3 wdp.py

python3 wdp.py -s 1700 -e 2200
```
In script, you can press 0 to 7 to answer, q to quit and press any other key to show next date.


## Note for The Doomsday Algorithm

### 1. Doomsday

Those Doomsday have same day of week.
- 1/3 or 1/4 on leap years
- 2/28 or 2/29 on leap years
- 3/14
- 4/4
- 5/9
- 6/6
- 7/11
- 8/8
- 9/5
- 10/10
- 11/7
- 12/12

E.g. on 2000, those Doomsday are Tuesday.

### 2. Years

- 1700 -> 0
- 1800 -> 5
- 1900 -> 3
- 2000 -> 2
- 2100 -> 0
- 2200 -> 5
- 2300 -> 3
- 2400 -> 2

Years add 28 will not change weekday on Doomsday. e.g. 2000, 2028, 2056 and 2084 have same weekday on Doomsday.

Years add 12 will change weekday by 1. e.g. 2000 -> 2, 2012 -> 3, 2024 -> 4.
