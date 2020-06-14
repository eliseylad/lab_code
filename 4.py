def sr(*args):
    print(sum(args)/len(args))
def prnt(**kwargs):
    print(kwargs)

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
