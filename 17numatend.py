import re
def check(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(check('salta'))
print(check('salta6'))
