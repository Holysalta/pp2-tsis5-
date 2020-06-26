import re
def check (stri):
    charr = re.compile(r'[^a-zA-Z0-9.]')
    stri = charr.search(stri)
    return not bool(stri)

print(check("ABCD")) 
print(check("*"))
