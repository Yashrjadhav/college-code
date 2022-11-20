arr=[]
m=int(input("ENTER TOTAL NUMBER OF STUDENTS, PERCENTAGE YOU WANT TO SORT:"))
for k in range(m):
    n = float(input("ENTER THE PERCENTAGE OF FIRST YEAR STUDENT :"))
    arr.append(n)
def selection():
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                min=j
        if min !=i:
            temp =arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    print("THE SORTED ARRAY BY SELECTION SORT IS: ",arr)

def bubble1():
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]>=arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("THE SORTED ARRAY BY BUBBLE SORT IS: ",arr)
l=0
while(l==0):
    choice=int(input('''ENTER WHICH SORT YOU WANT TO PERFORM:\n PRESS 1: SELECTION SORT \n PRESS 2: BUBBLE SORT''' ))
    if (choice==1):
        selection()
    if(choice==2):
        bubble1()
    elif(choice!=1 and choice!=2):
        print("INVALID INPUT ENTERED!!!")
        l=1
        break




