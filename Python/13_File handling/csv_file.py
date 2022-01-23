from csv import writer
import csv
from csv import reader
default_text = 'Some Text'
list_of_str = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
# Open the input_file in read mode and output_file in write mode
def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)
print('\nInput File :\n')
file = open("input.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
for row in rows:
    print("\n",row)
file.close()

with open('input.csv', 'r') as read_obj, \
        open('output_1.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)
    # Read each row of the input csv file as list
    for row in csv_reader:
        # Append the default text in the row / list
        row.append(default_text)
        # Add the updated row / list to the output file
        csv_writer.writerow(row)
add_column_in_csv('input.csv', 'output_1.csv', lambda row, line_num: row.append(list_of_str[line_num - 1]))

print('\nOutput File :\n')
file = open("output_1.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
for row in rows:
    print("\n",row)
file.close()