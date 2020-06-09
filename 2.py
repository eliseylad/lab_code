a=3
b=5
print(a, id(a), b, id(b), sep='|')
a=b
a=10
print(id(a), id(b), sep='|')
print("Изначально id(a)  становится равным id(b) а потом id(10), id(b) тем временем не меняется")
list1=[1,2]
list2=list1
print("list1")
for item in list1:
    print(item, id(item), sep='|')
print("list2")
for item in list2:
    print(item, id(item), sep='|')

list2[1]=10
print("list1")
for item in list1:
    print(item, id(item), sep='|')
print("list2")
for item in list2:
    print(item, id(item), sep='|')
print("list1 и list2 это объекты, когда мы изменяем list2[1], мы изменяем это значение у объекта, на которое указывает так же list1")

a=3
b=2
print(a+b, a-b,a*b,a/b,a//b,a**b, sep='|')
print(a&b,a|b, sep='|')
print(" я так понимаю, что логическое и берет общую часть т.е и в 2 и в 3 точно есть 2, а логическое или берет полный промежуток т.е 3 ")