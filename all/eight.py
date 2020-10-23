# BDD
# ===
# input              behavior               output
# [1,2,3],5           2+3 =5                  [1,2]
# [2,2,3], 4          2+2 =4                  [0,1]
#   i=0
#   j = i+ 1
# d ={ 
#     1: 0,                       [d[2], index(3)]        [1, 2]
#     2: 1,

# }
# pseudocode
# 1.create a fxn that takes two parameters
# 2.create a dictionary d and array results
# 3. loop through the llist and check if target - item is in the dictionary
# 4.  if it is then we want to return the index of item and also the value of the dict with same key
# 5. we want to add it to the dict
def TwoSums(nums, target):
    d={}
    arr = []
    for i in range(len(nums)):
        if target -  nums[i] in d:

            arr.append(d[target -  nums[i]])
            arr.append(i)
        else:
            d[nums[i]] = i
    return arr
# pseudocode
# 1.creste fxn takes two parameters- nums and target
# 2. loop thorough from i = 0 to the end of array
# 3. loop through the array again from  j = i+ 1 tp the end of array
# 4. check if item at i + item at j  = target
# 5. return i and j as our index

# def TwoSums(nums, target):    O(n^2)  O(1)
#     results = []
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 results.append(i)
#                 results.append(j)
#     return results
print(TwoSums([2,2,3], 4))