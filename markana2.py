#student marks analyzer
#input 10 std mrks
#using list methods and comprehension
#cal avg,find highest&lowest marks
#remove any dupli marks
#all above average in new list
#print everything in a formatted report

marks=[int(input("Enter the mark(out of 600):")) for i in range(10)]
t=sum(marks)
avg=t/len(marks)
highmark=max(marks)
lowestmark=min(marks)
print("Average mark is",avg)
print("highest mark is",highmark)
print("Lowest mark is",lowestmark)
a=set(marks)
u=list(a)
print(u)