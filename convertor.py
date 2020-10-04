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

def decToBase(decNum:int, base:int) -> int:
  """
  Pass a written integer in base 10
  Pass the numeral system radix | counting base
  (1-9 A-Z so base < 37)
  Get your number in the base you chose in return
  """
  strBase = ""
  dictToBe = {}
  helperString=list(range(10))+list(string.ascii_uppercase)

  for i in range(base):
    ch=helperString[i]
    dictToBe[i] = ch

  q = decNum
  while q!=0:
    r = q%base
    q//=base
    strBase = str(dictToBe[r]) + strBase

  return(strBase)
#examples
#print(baseToDec("A12",16))
#print(decToBase(35631,16))