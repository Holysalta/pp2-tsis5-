import re


words = ["Panda Panda", "Salta Salta", "c c++"]

for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            print(m.groups())