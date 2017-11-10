# Import csv
import csv
# Import os
import os

# Main Function
def main():
# Open dataset file
    dataset = open('./my files/morphII_cleaned_v2.csv', newline='')

# Initialize csvreader for dataset
reader = csv.reader(dataset)

# Read data from reader
data = list(reader)

# Variables for progress counter
lines = len(data)
i = 0

# Analyze data in dataset
for row in data:
    # Assign image name and state to variables
    image = row[0] + '.jpeg'
    state = row[1]

    # Print image information
    print('({}/{}) Processing image ({}): {}'.format(i + 1, lines, state, image))

    # Increment i
    i += 1

    # Determine action to perform
    if state is '0':
        # Attempt to move the file
        try:
    # Move the file to nosymptoms/