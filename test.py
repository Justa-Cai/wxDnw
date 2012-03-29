import os
import sys
data=(1,2,3,4)
a,b,c,d = data
print data
print a,b,c,d
sys.exit(0)
if os.path.isfile("./test_A.img"):
    os.remove("./test_A.img")
    
i=0
f = open("./test_A.img", "w")
while i<1024*1024:
    f.write('a')
    i+=1
f.close()
    