import readchar
from time import monotonic_ns as time
from collections import defaultdict

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
  letters = 'qwertyuiopasdfghjklzxcvbnm'
  for l1 in letters:
    for l2 in letters:
      if (l1, l2) in deltas:
        times = deltas[(l1, l2)]
        avg_sec = sum(times)/len(times)*(10**-9)
        print('{}, {}: {}'.format(l1, l2, avg_sec))

print("How many characters would you like to record?")
num = int(input())
print('Ok, begin typing!')
print_averages(record_characters(num))
