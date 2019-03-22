import csv
with open('timings.csv') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',')
    keys = []
    for row in spamreader:
        chars = row["key_seq"]
        if chars not in keys:
            keys.append(chars)
    print(len(keys))
    print(keys)
    print(26*26*26)
