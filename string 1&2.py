#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
  return 'Hello'+ ' '+name+"!"

#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba(a, b):
  return a+b+b+a
#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'

#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
def make_out_word(out, word):
  return out[0:2]+word+out[2:4]

#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
def extra_end(str):
  return str[len(str)-2:len(str)]*3
#Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
  if len(str)==0:
    return str
  else:
    return str[0:2]
  
#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
  return str[:len(str)/2]
#Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
  return str[1:len(str)-1]
  if len(str)==0:
    return str
#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
  if len(a)<len(b):
    return a+b+a
  else:
    return b+a+b
#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
  return a[1:len(a)]+b[1:len(b)]
#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

def left2(str):
  a=len(str)
  return str[2:a]+str[0:2]
#Given a string, return a string where for every char in the original, there are two chars
def double_char(str):
  rek=""
  for i in range(len(str)):
      
      rek=rek+str[i]*2
  return rek
#Return the number of times that the string "hi" appears anywhere in the given string
def count_hi(str):
  count=0
  for i in range(len(str)-1):
    check=str[i]+str[i+1]
    if check=='hi':
      count+=1
    else:
      count+=0
  return count
#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
  cat=0
  dog=0
  for i in range(len(str)):
    if str[i:i+3]=='cat':
      cat+=1
    if str[i:i+3]=='dog':
      dog+=1
  if cat==dog:
    return True
  else:
    return False

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  count=0
  for i in range(len(str)-3):
    if str[i:i+2]+str[i+3]=='coe':
      count+=1
  return count
      
#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
    a = a.lower()
    b = b.lower()
        
    return a.endswith(b) or b.endswith(a)
#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
    if str[:3] == "xyz":
        return True
                    
    for i in range(1, len(str) - 2):
        if str[i-1] != "." and str[i:i+3] == "xyz":
            return True
                                      
    return False





















































