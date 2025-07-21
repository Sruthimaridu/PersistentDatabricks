import os
#check if file exists
if os.path.exists('file.txt'):
    print('file exists')
    #get file size
size=os.path.getsize('file.txt')
print(size)

#get file modification time
import time
mod_time=os.path.getmtime('file.txt')
readable_time=time.ctime(mod_time)
print(mod_time)
print(readable_time)
