"""
BDD
---
input                       behavior                        output
abbac                       a,a  b,b  c                         c 
abacabad                    a,a,a,a  b,b  c  d                  c 
abba                        a,a  b,b                            _

 abbac
 d= {                       d[key] = 1   => key else _
     a: 2
     b: 2
     c: 1
 }

 pseudocode
 1.create fxn first_not_repeating_character and takes a string as parameter
 2.create the dictionary
 3. check if key is inside dictionary
 4. If it's inside dictionary then increment by 1
 5. else I want to intialize the key with 1 as value
 6. check if dictionary has the value 1
 7. if it does I want to return the key
 8. Else I want to return first_not_repeating_character



"""



def first_not_repeating_character(s):
    d=dict()
    for c in s:
        if d.get(c):
            d[c] +=1
        else:
            d[c] = 1
    for c in s:
        if d[c] == 1:
            return c 
    return "_"    



print(first_not_repeating_character("abacbvv" ))