import re
def check(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check("Ramazanova"))
print(check("Zaltanat"))