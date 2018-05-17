def getPalindrome():
  max = 0
  a = 99
  i = 999
  k = 999
  while i < a:
    i -= 1
    while k < a:
      k -= 1
      n = i * k
      s = '' + n
      if s == s.split("").reverse().join("") and n > max:
        max = n
  return max

print(getPalindrome());