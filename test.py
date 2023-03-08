import numpy as np
from pydub import AudioSegment  # reference at bottom
import csv
import sys

def main():
    # filepath = input("Please enter the path to your audio file: ")
    try:
        with open("tuning.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            tuning = {row['Note']: float(row['Frequency']) for row in reader} # create dictionary for all correct note values.. {"Note name": frequency}
    except FileNotFoundError:
        sys.exit("tuning.csv not found")
    print(tuning)


main()