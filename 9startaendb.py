import re
def check(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check("aabbbbd"))
print(check("aabAbbbc"))
print(check("accddbbjjjb"))