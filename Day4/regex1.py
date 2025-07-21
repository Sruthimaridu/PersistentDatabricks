import re
text="hello"
pattern=r"\d{3}-\d{3}-\d{4}"
match=re.search(pattern,text)
if match:
    print(f"found:{match.group()}")
    print(f"position:{match.start()}-{match.end()}")
##################################
text="123"
pattern=r"\d+"
if re.fullmatch(pattern,text):
    print("entire string matches")
text="contact me at any time"
pattern=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails=re.findall(pattern,text)
print(emails)