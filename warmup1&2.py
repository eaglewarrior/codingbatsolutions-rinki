#####warmup 1################

#The parameter weekday is True if it is a weekday, and the parameter
#vacation is True if we are on vacation. We sleep in if it is not a
#weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
  if a_smile==b_smile:
    return True;
  else:
    return False;

#Given two int values, return their sum. Unless the two values are the same, then return double their sum
def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21(n):
  diff=21-n;
  if n>21:
    diff1=n-21;
    diff=diff1*2
  return diff
    

#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  sum=a+b;
  if a==10 or b==10 or sum==10:
    return True
  else:
    return False

#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
def not_string(str):
  if str[0:3]=='not':
    return str
  else:
    return 'not '+str
  
#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


def missing_char(str, n):
  return str[0:n]+str[n+1:len(str)]

#########warm up 2##############


#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
  return str*n

#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
  return str[0:3]*n

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  result = ""
  
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
  res=""
  for x in range(len(str)):
    
    res=res+str[:x+1]
  return res
string_splosion('code')

#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count
#Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  return nums.count(9)
    

#
#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
def array_front9(nums):
  
  cor=nums[0:4].count(9)
  if cor!=0:
    return True
  else:
    return False

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count


