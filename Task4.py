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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def main():
    possible_telemarketers = {}
    # make a dictionary of all outgoing callers (to avoid duplicates)
    for call in calls:
        possible_telemarketers.update({call[0]: 0})
    # remove all call receivers and texters on either end from the dict
    for call in calls:
        remove_non_marketers(call[1], possible_telemarketers)
    for text in texts:
        remove_non_marketers(text[0], possible_telemarketers)
        remove_non_marketers(text[1], possible_telemarketers)
    # sort the list lexicographically
    possible_telemarketers = sorted(possible_telemarketers)
    # final print of the list
    print("These numbers could be telemarketers: ")
    for caller in possible_telemarketers:
        print(str(caller))


def remove_non_marketers(phone_number, database):
    # helper function that removes any cleared numbers from the marketing list
    if phone_number in database:
        del database[phone_number]


main()




