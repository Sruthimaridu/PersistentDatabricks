#write string to file
with open('file.txt','w') as f:
    f.write("hello world")

#write multiple lines
lines=['line 1\n','line2\n','line3\n']
with open('file.txt','w') as f:
    f.writelines(lines)

#append to file
with open('file.txt','a') as f:
    f.write('\nAppended text')

