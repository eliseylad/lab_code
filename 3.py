nums=[-2,1,-3,4,-1,2,1,-5,4]
maxi=-1
tek=0
for tek1 in nums:
    if(maxi<0 and tek1>0): 
        maxi=tek1;
        tek=tek1;
    else:
        tek=tek+tek1
        if(tek>maxi): 
            maxi=tek            
        if(tek1>maxi):
            maxi=tek1
            tek=tek1            
print(maxi)