import re
def check(text):
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check("abb"))
print(check("aabbbbbc"))