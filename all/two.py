# 1. create a fxn
def first_non_repeating_character(s):
# 2. create dict
    d= dict()
# 3. loop through sentence and if it already exist in dictionary add 1 else if it doesn't then assign it a value 1
    for c in s:
        if d.get(c):
            d[c] += 1
        else:
            d[c] = 1
# 4. loop through the string
    for c in s:
#     return the char in the dict that has a value 1
      if d[c] == 1:
          return c  
# 5. else return "_"
    return "_"
print(first_non_repeating_character("abacbv" ))