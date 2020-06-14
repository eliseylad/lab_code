def sr(*args):
    print(sum(args)/len(args))
def prnt(**kwargs):
    print(kwargs)

def sdvig(nums,k):
    if(k>0):
        d=nums[len(nums)-1]
        i=len(nums)-1
        while(i>0):
            nums[i]=nums[i-1]
            i=i-1
        nums[0]=d
        sdvig(nums,k-1)
    else:
        print(nums)

def nul(nums,k,count):
    while(k<len(nums)-1-count):
        if(nums[k]==0):            
            i=k
            while(i<len(nums)-1):
                nums[i]=nums[i+1]
                i=i+1
            nums[len(nums)-1]=0           
            nul(nums,k,count+1)
            break
        k=k+1
nums=[1,2,3,4,5]
d=dict(name="elisey",age=20)
sr(*nums)
prnt(**d)

try:
    print(10/0)
except Exception as e:
    print("oh no! "+str(e))
finally:
    print("don't worry")

try:
    print(10/0)
except Exception as e:
    print("oh no! "+str(e))
else:
    print("wow")
print("finally будет выполнено в любом случае, а else только если ошибки не было")

sdvig(nums,-3)
#тесты:
#nums=[1,2,3,4,5,6,7] sdvig(nums,1) sdvig(nums,7) sdvig(nums,0) sdvig(nums,-1) sdvig(nums,-0) sdvig(nums,6)
#nums=[1,2] sdvig(nums,1) sdvig(nums,0) sdvig(nums,2) sdvig(nums,3) sdvig(nums,4) sdvig(nums,8) sdvig(nums,-2)
#nums=[1] sdvig(nums,0) sdvig(nums,1) sdvig(nums,2) sdvig(nums,5) sdvig(nums,-3) sdvig(nums,-5) sdvig(nums,-1)
nums=[0,0,3,0,12,13,2,2,2]
nul(nums,0,0)
print(nums)
#тесты
#nums=[0,5,0,5,0,4,3,0] nums=[0,0,0,0] nums=[1,2,3,4,5] nums=[0,0,0,1,2,3] nums=[6,0,9,0,8,0,0,6,5,6,3,4,6,0,0,0,0,3,4,6,0]