def reverse(text):
  s=""
  l=len(text)
  for i in range(l):
    s+=text[l-1-i]
  return s


#to make reverse a string without reversed() and [::-1]
