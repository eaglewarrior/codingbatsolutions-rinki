#When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
def cigar_party(cigars, is_weekend):
  if (40<=cigars<=60) and (is_weekend==False) :
    return True
  if 40<=cigars and is_weekend==True:
    return True
  else:
    return False
#You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

def date_fashion(you, date):
  if (you>8 and date>2) or (you>2 and date>8):
    return 2
  if (you<=2 or  date<=2):
    return 0
  else:
    return 1
#The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

def squirrel_play(temp, is_summer):
  if (60<=temp<=90 and is_summer==False) or (60<=temp<=100 and is_summer==True):
    return True
  else:
    return False
#You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
  if (speed<=60 and is_birthday==False) or (speed<=65 and is_birthday==True):
      return 0
  if (61<=speed<=80 and is_birthday==False) or (66<=speed<=85 and is_birthday==True):
    return 1
  if (81<=speed and is_birthday==False) or (86<=speed and is_birthday==True):
    return 2
#Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def sorta_sum(a, b):
  sum=a+b
  if 10<=sum<=19:
    return 20
  else:
    return sum

#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
  if (1<=day<=5 and vacation==False):
    return '7:00'
  if (day==0 or day==6) and (vacation==False):
    return '10:00'
  if (day==0 or day==6) and (vacation==True):
    return 'off'
  if (1<=day<=5 and vacation==True):
    return '10:00'
  
#The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

def love6(a, b):
  if (a==6 or b==6) or (a+b==6) or (a-b==6) or (b-a==6):
    return True
  return False
#Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
def in1to10(n, outside_mode):
  if (1<=n<=10 and outside_mode==False) or ((n<=1 or n>=10) and outside_mode==True):
    return True
  return False

#Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
def near_ten(num):

    a = num % 10
    if  (10 - (10-a)) <= 2 or (10 - a) <= 2:
        return True
    else:
        return False


#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.
def make_bricks(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - (5 * big)
    else:
        remainder = goal % 5
        
    return small >= remainder
#Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
  if a==b==c:
    return 0
  if a==b :
    return c
  if a==c:
    return b
  if b==c:
    return a
  else:
    return a+b+c
#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
  sum = 0
  list = [a,b,c,13]
  for n in list[:list.index(13)]:
    sum += n
  return sum
#Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
def no_teen_sum(a, b, c):
  
  def fix_teen(n):
    return n if n not in [13,14,17,18,19] else 0

  return fix_teen(a)+fix_teen(b)+fix_teen(c)

#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
def round10(num):
  if num%10>=5:
    return num+(10-num%10)
  else:
    return num-(num % 10)
#Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(a, b, c):
  return (abs(abs(b)-abs(c))>=2) and \
  ((abs(abs(b)-abs(a))<=1 and abs(abs(c)-abs(a))>=2) \
  or (abs(abs(c)-abs(a))<=1 and abs(abs(b)-abs(a))>=2))
#We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
        
    if remainder <= small:
        return remainder
        
    return -1



































