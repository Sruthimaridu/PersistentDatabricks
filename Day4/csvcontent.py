import csv
data = [
    ['Name', 'Age', 'City'],
    ['sruthi', 21, 'ap'],
    ['deepu', 15, 'uk'],
    ['surya', 9, 'Paris']
]
filename = 'people.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data has been written to '{filename}'")
