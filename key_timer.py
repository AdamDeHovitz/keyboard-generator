import readchar
import json
from time import monotonic_ns as time
from collections import defaultdict
from verifier import verify, letters

converter = {}
for i, letter in enumerate(letters):
  converter[letter] = str(i)

def convert(letter):
  return converter[letter]

def record_words(file_path):
  p = None
  count = 0
  c_time = None
  deltas = defaultdict(list)
  with open(file_path) as f:
    for word in f.read().split(' '):
      failures = 0
      success = False
      while success is False:
        failures += 1
        if failures > 5:
          exit()
        print(word)
        typed = ''
        c_time = None
        while len(typed) < len(word):
          c = readchar.readchar()
          if not c.isalpha():
            break
          typed += c
          p_time = c_time
          c_time = time()
          if p_time is not None:  
            deltas[(p, c)].append(c_time - p_time)
          p = c
        if typed == word:
          success = True
  return deltas

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
    d[convert(i)+','+convert(j)] = k
  return json.dumps(d)

def save_deltas(json_dict, file_path):
  with open(file_path, 'a+') as f:
    f.write(json_dict)
    f.write('\n')
    print("Saved!")

if __name__ == "__main__":
  file_path = 'times.txt'
  corpus_path = 'corpora/timer_corpus.txt'
  print('Type the following words, to exit press enter, and if u fuck up press enter:')
  #print_averages(record_characters(num))
  deltas = record_words(corpus_path)
  if not verify(deltas.keys()):
    print('Corpus does not have all pairs. Exiting.')
    exit()
  save_deltas(json_convert(scale(deltas)), file_path)
