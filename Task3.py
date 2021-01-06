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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def main():
    bangalore_incoming = []
    area_codes = []
    # make a list of all prefixes of the calls that are coming out of bangalore
    for item in calls:
        if item[0].startswith("(080)"):
            area_codes.append(get_prefixes(item, bangalore_incoming))
    # Remove duplicates and sort lexicographically (storing in separate list so OG can be used to calc %)
    area_codes_sorted = sorted(set(area_codes))
    # print part A
    print("The numbers called by people in Bangalore have codes:")
    for area_code in area_codes_sorted:
        print(str(area_code))
    # calculate percentage of outgoing bangalore calls
    percentage = round(((len(bangalore_incoming) / len(area_codes)) * 100), 2)
    # print part B
    print(str(percentage) + " percent of calls from fixed lines in Bangalore are calls "
                            "to other fixed lines in Bangalore.")


def get_prefixes(item, bangalore_incoming):
    # returns the prefix, and adds one to the bangalore list
    if item[1].startswith("1"):
        return "140"
    elif item[1].startswith("("):
        if item[1].startswith("(080)"):
            bangalore_incoming.append(1)
            return "080"
        else:
            second_parentheses = item[1].find(")")
            prefix = item[1][1:second_parentheses]
            return prefix
    # to mobile
    elif item[1].startswith("7") or item[1].startswith("8") or item[1].startswith("9"):
        prefix = item[1][:4]
        return prefix


main()
