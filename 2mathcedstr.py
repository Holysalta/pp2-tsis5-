import re
def check(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check("ac"))
print(check("abc"))
print(check("abBc"))