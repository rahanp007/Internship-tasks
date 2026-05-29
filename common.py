#step1:takes two list from user
#step2:converts them into sets
#step3:finds common elements between both sets(intersection)
list1=[]
list2=[]
for i in range(5):
    a=int(input("Enter your elemests:"))
    list1.append(a)
for i in range(5):
    b=int(input("Enter your elements:"))
    list2.append(b)
s1=set(list1)
s2=set(list2)
print(s1)
print(s2)
i=s1.intersection(s2)
print(i)
