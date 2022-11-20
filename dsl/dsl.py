l=[]
def student():
    n=int(input("ENTER THE TOTAL NUMBER OF STUDENTS:"))
    for i in range(n):
        l.append(int(input("ENTER ROLL NUMBER OF STUDENTS:")))
    print("THE ROLL.NOS ARE:")
    for i in l:
        print("[",i,"]")
def linear():
    count=0
    k=int(input("ENTER THE ROLL NUMBER OF STUDENT TO CHECK WHETHER STUDENT WAS PRESENT \n AT THE TRAINING PROGRAM: "))
    for i in range(len(l)):
        if k==l[i]:
            print("STUDENT WAS PRESENT FOR THE PROGRAM AT POSITION: " ,i)
            break
        else:
            count+=1
    if (count-1==i):
        print("STUDENT WAS ABSENT FOR THE PROGRAM ")
def sentinal():
    y = int(input("ENTER THE ROLL NUMBER OF STUDENT TO CHECK WHETHER STUDENT WAS PRESENT \n AT THE TRAINING PROGRAM: "))
    last=l[-1]
    l[-1]=y
    i=0;
    while(y!=l[i]):
        i+=1
    l[-1]=last
    if (i<len(l)-1 or y == l[-1]):
        print("STUDENT WAS PRESENT FOR THE TRAINING PROGRAM AT POSITION:",i)
    else:
        print("STUDENT WAS ABSENT FOR THE PROGRAM ")
student()
m=0
while (m==0):
    a=int(input("ENTER THE TYPE OF SEARCH YOU WANT TO PERFORM: \n PRESS1: LINEAR SEARCH \n PRESS2: SENTINAL SEARCH \n PRESS 3: EXIT"))
    if a==1:
        linear()
    if a==2:
        sentinal()
    if a==3:
        m==1
        break


