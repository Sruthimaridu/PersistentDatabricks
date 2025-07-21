import re
def valid_url(url):
    pattern= r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(pattern,url)
url=input("enter url: ")
if valid_url(url):
    print("valid")
else:
    print("not valid")

