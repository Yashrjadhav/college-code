list1=[]
list2=[]
marks=[]
n=int(input("ENTER THE TOTAL NUMBER OF STUDENTS IN THE CLASS: "))
for i in range(n):
    marks.append(int(input("ENTER THE MARKS OF STUDENTS SCORED IN THE TEST: ")))
for i in marks:
    if i!=-1:
        list1.append(i)
    else:
        list2.append(i)
print("THE NO .OF STUDENTS WHO WERE PRESENT FOR THE TEST ARE:",len(list1))
print("THE NO .OF STUDENTS WHO WERE ABSENT FOR THE TEST ARE:",len(list2))
def average():
    sum=0
    for i in list1:
        sum=sum+i
    print("THE AVERAGE OF STUDENTS MARKS IS",sum/len(list1))
def maximum():
    max=list1[0]
    for i in list1:
        if max<i:
            max=i
    print("THE MAXIMUM OR HIGHEST SCORE IN TEST IS:",max)
def minimum():
    min=list1[0]
    for i in list1:
        if min>i:
            min=i
    print("THE MINIMUM OR LOWEST SCORE IN TEST IS:",min)
def highfreq():
    g=marks[0]
    count=0
    for i in marks:
        a=marks.count(i)
        if a>count:
            count=a
            g=i
    print("THE HIGHEST FREQUENCY OF MARKS",g)
while True:
    s=int(input('''ENTER YOUR CHOICE:
    PRESS 1:THE MAXIMUM SCORE IN THE TEST
    PRESS 2:THE MINIMUM SCORE IN THE TEST 
    PRESS 3:THE AVERAGE STUDENTS MARKS 
    PRESS 4:THE HIGHEST FREQUENCY OF SCORE\n'''))
    if s==1:
        maximum()
    if s==2:
        minimum()
    if s==3:
        average()
    if s==4:
        highfreq()
    j=int(input(('''DO YOU WANT TO ENTER DIFFERENT CHOICE:\nIF YES: ENTER 1\nIF NO : ENTER 0:\n''')))
    if j!=1:
        break