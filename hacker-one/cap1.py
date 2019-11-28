#import wget
import os
#path1="/Users/vaibhav/Desktop/database/cet2020/CAP2/"
file=open("/Users/vaibhav/Desktop/database/cet2020/CAP1/reg_no_college.txt","a")
data=[]

for num in range(1002,6939):
    if os.path.exists("/Users/vaibhav/Desktop/database/cet2020/CAP1/CAPR-I_EN"+str(num)+".pdf"):
        data.append(num)
        
    else:
        pass
    
print(data)
print(len(data))
    
    