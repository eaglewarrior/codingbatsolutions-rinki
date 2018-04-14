#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
  if nums[0]==6 or nums[len(nums)-1]==6:
    return True
  else:
    return False
#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
def same_first_last(nums):
  if len(nums)>=1 and nums[0]==nums[len(nums)-1]:
    return True
  else:
    return False
#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
  return[3,1,4]
#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
  if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
    return True
  else:
    return False
#Given an array of ints length 3, return the sum of all the elements.

def sum3(nums):
  sum=0
  for i in range(len(nums)):
    sum=sum+nums[i]
  return sum

#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
  return nums[1:len(nums)]+[nums[0]]
#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
  return nums[::-1]
#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
  if nums[0]>nums[len(nums)-1]:
    return [nums[0]] *(len(nums))
  else:
     return [nums[len(nums)-1]] *(len(nums))
#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
  if len(nums)==2:
    return sum(nums)
  else:
    return sum(nums[0:2])
  
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a, b):
  return [a[1]]+[b[1]]
#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
def make_ends(nums):
  return [nums[0]]+[nums[len(nums)-1]]
#Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
  if (nums[0]==2 or nums[0]==3) or (nums[1]==2 or nums[1]==3):
    return True
  else:
    return False
#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
  count=0
  for i in range(len(nums)):
    if nums[i]%2==0:
      count+=1
  return count
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
  b=sorted(nums)
  l=len(b)
  return b[l-1]-b[0]
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(nums):
  nums.sort()
  return sum(nums[1:-1]) / (len(nums) - 2)
#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
    s = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 1
        else:
            s += nums[i]
            
        i += 1
        
    return s
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
    record = True
    total = 0

    for n in nums:
        if n == 6:
            record = False

        if record:
            total += n
            continue

        if n == 7:
            record = True

    return total
#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
  if len(nums)==0:
    return False
  for i in range(len(nums)-1):
    #print nums[i:i+2]
    if nums[i:i+2]==[2,2]:
      return True
  return False

























