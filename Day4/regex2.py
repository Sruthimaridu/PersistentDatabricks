import re
text="hello world"
pattern=r"hello"
match=re.match(pattern,text)
if match:
    print("match found")
else:
    print("no match found")