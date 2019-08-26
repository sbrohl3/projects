import json
import csv

## Importing the text file for cleaning then converting to CSV
input_file = open("text_files/customer_export.txt", "r")
output_file = open("text_files/customers.csv", "w")

for line in input_file:
    clean_text = ""
    check_line = line.replace("#", "").replace(",,","").split("|")
    for line in check_line:
        if line != check_line[10]:
            clean_text += line + ","
        elif line == check_line[10]:
            clean_text += line + "\n"
            output_file.write(clean_text)

## Closing TXT file and CSV file after formatting
input_file.close()
output_file.close()

## Opening the cleaned CSV file for conversion to Json
with open('text_files/customers.csv') as clean_csv:
    ## Converting CSV file to Json
    convert = csv.DictReader(clean_csv)
    rows = list(convert)

## Writing converted CSV to Json file
with open('text_files/customers.json', 'w') as convert:
    json.dump(rows, convert)
