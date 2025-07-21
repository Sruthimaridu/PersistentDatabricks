import json

'''#reading json
with open('data.json','r')as f:
    data=json.load(f)'''

'''#write json
data={'name': 'alica','age':30,'class': "betch"}
with open('data.json','w') as f:
    json.dump(data,f,indent=5)'''

#binary files
#reading binary file
with open('forest.jpg','rb') as f:
    binary_data=f.read()

#writing binary file
with open('forest.jpg','wb') as f:
    f.write(binary_data)

