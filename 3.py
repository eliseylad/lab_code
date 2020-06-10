nums=[-2,1,-3,4,-1,2,1,-5,4]
maxi=nums[0]
num=0
tek=0
for tek1 in nums:    
    if(num>0):
        tek=tek+tek1
        if(tek>maxi): 
            maxi=tek            
        if(tek1>maxi):
            maxi=tek1
            tek=tek1   
    num=1         
print(maxi)
num2 = [[1,3],[2,6],[8,10],[15,18]]
num2.sort(key=lambda x: (x[0], x[1]))
itog=list()
prom=num2[0]
for tek in num2:
    if ( prom[0]<tek[0] and prom[1]>tek[0] and tek[1]>prom[1] ):
        prom[1]=tek[1]        
    else:
        itog.append(tek)
        prom=tek    
for tek in itog:
    print(tek[0],tek[1])