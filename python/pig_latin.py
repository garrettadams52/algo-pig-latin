import re

def translate(word_or_phrase):
  lst = word_or_phrase.split()
  vow = 'aeiou'
  ans = []
  str1 = ''
  
  for x in lst:
    x=list(x)
    if x[0] in vow:
      x.pop(0)
      x.append('ay')
    ans.append(x)

  #str1.join(ans)

  print(ans)

print(translate('atesting the phrase'))