List1=[]
for i in range(5):
    a=int(input('Enter a num upto 5: '))
    List1.append(a)
print(List1)
largest=max(List1)
smallest=min(List1)
total=sum(List1)
print(largest,",", smallest,",", total)
even=0
odd=0
for num in List1:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers:",even)        
print("Odd numbers:",odd)
     