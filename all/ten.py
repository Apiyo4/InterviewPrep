# # Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# # For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# BDD
# ----
# input                          behaviour                         output
# [10,15,3,7], 17                    10 + 7 =17                                 true

# d={ 10: 0,
#     15: 1,                      return true
#     3: 2,

# }
# Pseudocode
#  1.create a fxn taht takes in an array and K
#  2. create a dictionary taht holds the values
    #  loop through array
#  3. check if the difference btn element and k exists in the dictionary
#  4. if it does return True
#  5.else insert the element and index in the dict

def AddsUpToK(arr, k):
    d= dict()
    
    for i in range(0,len(arr)):

        if k - arr[i] in d:
            print(k - arr[i])
            return True
        else:
            d[arr[i]] = i

    return False
# i and j
# i = 0 , j= i+1
# 10 +15 = 25, 15+3= 18, 3+7=10, 10 +7
# # 15 + 3 = 18, 15+7 = 22

# Pseudocode
# 1.create a fxn taht takes in a an array and K
# 2. loop through the array from i=0 to the end
# 3. loop through the array from j= i+1 to the end
# 4. check if element i + element j equals k
# 5. if true return true
# 6. return False


# def AddsUpToK(arr, k):
#     for i in range(0, len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == k :
#                 return True
        
#     return False

print(AddsUpToK([10,15,3,7], 17))


