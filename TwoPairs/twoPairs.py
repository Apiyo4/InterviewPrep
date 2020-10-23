"""
Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.
BDD
---
input                               output

[3, 5, 2, -4, 8, 11], 7         [[2,5], [-4, 11]]

d = { 3 : 0,            [[2,5], [11,-4]]
      5 : 1,
      -4 : 3,
       8: 4
}
pseudocode
---------
1. create a fxn take arr and s,
2. create a dictionary  d and arr results,
3.  loop through the array
4.   check if s-item is in the dictionary
5.    we want the two inside results  results.append([s-item, item])
6.  add item to dictionary
7. return results

"""

def FindAllPairs(arr, s):
  d ={}
  results = []
  for i in range (0, len(arr)):
    if d.get(s-arr[i]):
      d[arr[i]] = i
      results.append([arr[i], s-arr[i]])
    else:
      d[arr[i]] = i   

  return results

print(FindAllPairs([3, 5, 2, -4, 8, 11], 7  ))