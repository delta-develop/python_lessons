


def counter(strings, queries):
    strings_dict = {}
    result = []
    for string in strings:
        if string in strings_dict:
            strings_dict[string] += 1
        
    
    print(strings_dict)
    
    for query in queries:
        if strings_dict.get(query):
            strings_dict[query] += 1
    
    for string in strings:
        result.append(strings_dict[string])
        
    return result


strs = ["abc","ab","abc"]
queries = ["ab","abc","bc"]

print(counter(strs,queries))