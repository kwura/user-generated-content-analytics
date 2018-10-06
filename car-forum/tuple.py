import csv
with open('finalcomments.csv') as f:
    data=[tuple(line) for line in csv.reader(f)]

print(len(data))
print(data[-1])