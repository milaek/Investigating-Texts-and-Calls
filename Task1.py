"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def main():
    # make a new dictionary(to avoid duplicates) with all phone numbers
    phone_numbers = {}
    for text in texts:
        phone_numbers.update({text[0]: 0, text[1]: 0})
    for call in calls:
        phone_numbers.update({call[0]: 0, call[1]: 0})
    # print statement with the length of the list w/o duplicates
    print("There are " + str(len(phone_numbers)) + " different telephone numbers in the records.")


main()

