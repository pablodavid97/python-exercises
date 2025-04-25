import math
import os
import random
import re
import sys
from datetime import datetime
import pytz

def time_delta(t1, t2):
    format_str = '%a %d %B %Y %H:%M:%S %z'

    date1 = datetime.strptime(t1, format_str)
    date2 = datetime.strptime(t2, format_str)

    utc1 = date1.astimezone(pytz.utc)
    utc2 = date2.astimezone(pytz.utc)
    time_difference = (utc1-utc2).total_seconds()

    return f'{time_difference}'

def main():
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    else:
        # When running locally, print to console instead
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

if __name__ == '__main__':
  main()