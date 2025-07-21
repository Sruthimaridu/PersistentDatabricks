#replace matches
import re
text="the date is 2025-07-17"
pattern=r"(\d{4})-(\d{2})-(\d{2})"     #
r=r"\2/\3/\1"
new=re.sub(pattern,r,text)
print(new)

#split string by pattern
text="apple,banana:orange;grape-mango"
pattern=r"[,:;-]"
parts=re.split(pattern,text)
print(parts)

#digits
p=r"\d+"
t="i have 25 apples"         #25
print(re.findall(p,t))

#word character (letters,digits,underscore)
p=r"\w+"
t="hello world 123"                #["hello","world",123]   
print(re.findall(p,t))

#whitespaces
p=r"\s+"
t="hello  world"                   #["hello", "world"]
print(re.split(p,t))