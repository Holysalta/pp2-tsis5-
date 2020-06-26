import re
def check(text):
        patterns = '^[a-z]+_[a-z]+$'
        if not re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check("aab_cbbbc"))
print(check("aab_Abbbc"))
print(check("Aaab_abbbc"))