list_marks=[]
passed=0
failed=0
for i in range(5):
    a=int(input("Enter your marks:"))
    list_marks.append(a)
Highest_Marks=max(list_marks)
Lowest_Marks=min(list_marks)
Avg=sum(list_marks)/len(list_marks)
for marks in list_marks:
    if marks>=40:
        passed+=1
    else:
        failed+=1
print("highest mark",Highest_Marks)
print("lowest mark",Lowest_Marks)
print("average",Avg)
print(f"{passed} students passed, {failed} students failed")