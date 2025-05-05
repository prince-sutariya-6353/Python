import csv

# Writing to a CSV file
data = [
    ['Name', 'Age', 'City'],
    ['ram', 22, 'Surat'],
    ['prince', 25, 'kim']
]

with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
