import json

# Convert Python dict to JSON string
x = {"name": "pravalika", "age": "22"}
y = json.dumps(x)  # Convert Python dict to JSON string

# Convert JSON string back to Python dict
z = json.loads(y)

print(z["name"])
print(z["age"])

# Another example
x1 = {
    "name": "xyz",
    "age": 35
}
y1 = json.dumps(x1)  # Convert Python dict to JSON string
print(y1)
