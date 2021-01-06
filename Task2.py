"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def main():
    phone_times = {}
    # compile amount of time each phone spent on the phone
    for individual in calls:
        for i in range(2):
            if phone_times.get(individual[i]) is not None:
                new_time = int(phone_times.get(individual[i])) + int(individual[3])
            else:
                new_time = int(individual[3])
            phone_times.update({individual[i]: new_time})

    # sort by times into reverse order
    sorted_times = sorted(phone_times.items(), key=lambda x: x[1], reverse=True)

    # final print statement
    print(str(sorted_times[0][0]) + " spent the longest time, " + str(sorted_times[0][1]) +
          " seconds, on the phone during September 2016")


main()



