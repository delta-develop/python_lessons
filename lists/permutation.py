import json

def permutation(str1,str2):
    
    str_1_char_count = {}
    str_2_char_count = {}
        
    for char in str1:
        if char not in str_1_char_count:
            str_1_char_count[char] = 1
        else:
            str_1_char_count[char] += 1
            
    for char in str2:
        if char not in str_2_char_count:
            str_2_char_count[char] = 1
        else:
            str_2_char_count[char] += 1    
            
    print(json.dumps(str_1_char_count,indent=2))
    print(json.dumps(str_2_char_count,indent=2))
    
    print(str_1_char_count == str_2_char_count)
    print(str_1_char_count is str_2_char_count)
    
    if str_1_char_count == str_2_char_count:
        return True
    return False


str1 = "holaamundo"
str2 = str1[::-1]
# str2 = "holamundoo"

print(permutation(str1,str2))