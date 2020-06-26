import re
def check(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(check('5-2345861'))
print(check('6-2345861'))