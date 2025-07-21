import re
def extract_phone_numbers(text):
    patterns = [
        r"\b\d{3}-\d{3}-\d{4}\b",           # 123-456-7890
        r"\b\(\d{3}\)\s*\d{3}-\d{4}\b",    # (123) 456-7890
        r"\b\d{3}\.\d{3}\.\d{4}\b",        # 123.456.7890
    ]
    nums=[]
    for pattern in patterns:
        nums.extend(re.findall(pattern,text))

    return nums
text="call me at any time"
print(extract_phone_numbers(text))

    