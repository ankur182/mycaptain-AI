# print positive Numbers in a List
  
# input of list
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)

print("Positive numbers in",li,"are: ")
  
#traversing
for i in li:   
    # checking condition
    if i >= 0:
       print(i, end = " ")