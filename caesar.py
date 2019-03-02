import enchant
import operator

d = enchant.Dict("en_US")

def breakCaesar(s):
  bruteforce = []
  s = list(s)
  x = 0
  while(x<(len(s)*25)):
    for i in range(len(s)):
      if (s[i] == 'Z'):
        s[i] = 'A'
      elif (s[i] == 'z'):
        s[i] = 'a'
      elif (s[i] == ' '):
        continue;
      else:
        s[i] = chr(ord(s[i]) + 1)
      x=x+1
    bruteforce.append(''.join(s))
  print (bruteforce)
  str_dict = []
  for i in bruteforce:
      counter = 0
      for j in i.split():
          if d.check(j):
              counter += 1
      str_dict.append([counter,i])
  index, value = max(enumerate([i[0] for i in str_dict]), key=operator.itemgetter(1))
  for i in str_dict:
      if i[0] == value:
          print i[1]


# breakCaesar("Ixfn Wklv Vklw")
