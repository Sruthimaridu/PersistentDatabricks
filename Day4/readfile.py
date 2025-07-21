#reading entite fie
with open('file.txt','r') as f:
    content=f.read()

#reading line by line
with open('file.txt','r') as f:
    for line in f:
        print(line.strip())  #remove newline characters 


#read all lines into list
with open('file.txt','r') as f:
    lines=f.readlines() #return list of lines

#read one line
with open('file.txt','r') as f:
    first_line=f.readline()

