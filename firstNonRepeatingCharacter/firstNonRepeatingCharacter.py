"""
input       output      behaviour
abacb       c           a, a ; b, b; c; 

Pseudocode
1.create a fxn first_non_repeating_character that take a string as args
2. create a dict d 
3. initialize the dictionary with keys as the char in s and value as 0
4. loop through the array (we get an item and also it's index) 
    loop through the array again (remove the item at the index and check if the item we got above occurs in the string)
5. get a list of keys and also values
6. check if value is contained in the values list; if yes then return the value 
    else return "-"

"""
# def first_non_repeating_character(s):
#     d ={}
#     n = set(s)
    
#     for c in n:
#         d[c] = 0

#     for c in s:
#         idx = s.index(c)
#         for a in s[idx: idx + 1]:
#             if a == c:
#                 d[a] += 1
#             else:
#                 d[c] += 0
    
#     key_list =  list(d.keys())
#     val_list =  list(d.values())

#     if 1 in val_list:
#         ans = key_list[val_list.index(1)]
        
#         return ans
#     else:
#         return "_"
# print(first_non_repeating_character("abacbc" ))

"""
pseudocode
1. create a fxn
2. create dict
3. loop through array and if it already exist in dictionary add 1 else if it doesn't then assign it a value 1
4. loop through the string
    return the char in the dict that has a value 1
5. else return "_"

"""
def first_non_repeating_character(s):
    d = {}
    for c in s:
        if d.get(c):
            d[c] +=  1
        else:
            d[c] = 1
    for c in s:
        if d[c] == 1:
            return c

    return "_"

print(first_non_repeating_character("abacbvvc" ))