import random
import tsv
import operator
from collections import OrderedDict

def main():
    file_name = "key:valueDB.tsv"
    date = input("Pick a date ranging from December of 2022 until September 2023:")
    pastNumbers = read_in_pastNumbers(key:valueDB.tsv)
    pastNumbers_arrays = analyze_pastNumbers(pastNumbers)

    # Retrieve the numbers for the selected date
    selected_numbers = pastNumbers_arrays[date]
    print(f"The win
