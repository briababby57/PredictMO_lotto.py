import random
import csv
import operator
from collections import OrderedDict

def main():
    file_name = "powerball.csv"
    date = input("Pick a date ranging from December of 2022 until September 2023:")
    pastNumbers = read_in_pastNumbers(file_name)
    pastNumbers_arrays = analyze_pastNumbers(pastNumbers)

    # Retrieve the numbers for the selected date
    selected_numbers = pastNumbers_arrays[date]
    print(f"The win
