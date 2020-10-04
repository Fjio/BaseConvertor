import string
def baseToDec(baseString:str, base:int) -> int:
  """
  Pass a written string in whatever base you want
  Pass the numeral system radix | counting base
  (1-9 A-Z so base < 37)
  Get your decimal number in return
  """
  num=0
  dictToBe = {}
  helperString=list(range(10))+list(string.ascii_uppercase)

  for i in range(base):
    ch=helperString[i]
    dictToBe["{}".format(ch)] = i

  for k in range(len(baseString)):
    num+=dictToBe[baseString[-(1+k)]]*(base**k)

  return(num)

#examples
print(baseToDec("A12",16))