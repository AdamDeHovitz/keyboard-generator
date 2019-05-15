import readchar
import json
from time import monotonic_ns as time
from collections import defaultdict
from verifier import verify, letters

converter = {}
for i, letter in enumerate(letters):
  converter[letter] = i

def convert(letter):
  return converter[letter]

def record_characters(num):
  p = None
  count = 0
  c_time = None
  deltas = defaultdict(list)
  while count < num:
    c = readchar.readchar()
    count += 1
    p_time = c_time
    c_time = time()
    if p_time is not None:  
      deltas[(p, c)].append(c_time - p_time)
    p = c
  return deltas

def print_averages(deltas):
  print('printing averages')
  for l1 in letters:
    for l2 in letters:
      if (l1, l2) in deltas:
        times = deltas[(l1, l2)]
        avg_sec = sum(times)/len(times)*(10**-9)
        print('{}, {}: {}'.format(l1, l2, avg_sec))

def scale(deltas):
  averaged_deltas = {}
  for l1 in letters:
    for l2 in letters:
      if (l1, l2) in deltas:
        times = deltas[(l1, l2)]
        averaged_deltas[(l1, l2)] = sum(times)/len(times)
  scaling_factor = 1/sum(averaged_deltas.values())
  return {k:v*scaling_factor for k,v in averaged_deltas.items()}

def json_convert(deltas):
  d = {}
  for (i, j), k in deltas.items():
    d[i+','+j] = k
  return json.dumps(d)

def save_deltas(json_dict, file_path):
  with open(file_path, 'a+') as f:
    f.write(json_dict)
    print("Saved!")

if __name__ == "__main__":
  print("Where would you like to save your times? ")
  file_path = input()
  print("How many characters would you like to record?")
  num = int(input())
  print('Ok, begin typing!')
  #print_averages(record_characters(num))
  deltas = record_characters(num)
  if not verify(deltas.keys()):
    print('Corpus does not have all pairs. Exiting.')
    exit()
  save_deltas(json_convert(scale(deltas)), file_path)
