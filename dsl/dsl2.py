list = []
n=int(input("ENTER THE TOTAL NO.OF STUDENTS: "))
for i in range(n):
    list.append(int(input("ENTER THE ROLL NUMBER OF STUDENTS WHO ATTENDED THE PROGRAM IN SORTED ORDER: ")))
def binary_search(list, n):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list[mid] < n:
            low = mid + 1
        elif list[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1

def fib_search(list,n):
    length = len(list)
    first = -1
    x0 = 0
    x1 = 1
    x2 = 1
    while(x2 < length):
        x0 = x1
        x1 = x2
        x2 = x1 + x0
    while(x2 > 1):
        eleIndex = min(first + x0, length - 1)
        if list[eleIndex] < n:
            x2, x1 = x1, x0
            x0 = x2 - x1
            start = eleIndex
        elif list[eleIndex] >n:
            x2 = x0
            x1 = x1 - x0
            x0 = x2 - x1
        else:
            return eleIndex
    if (x1) and (list[length - 1] == n):
        return length - 1
    else:
        return -1


i=0
while(i==0):
    g=int(input("ENTER THE SEARCH YOU WANT TO PERFORM: \n PRESS1: BINARY SEARCH \n PRESS2: FIBONACCI SEARCH: \n PRESS3: EXIT "))
    n = int(input("ENTER THE ROLL.NO YOU WANT TO CHECK WHETHER WAS PRESENT OR ABSENT FOR THE TRAINING PROGRAM: "))
    if g==1:
        result = binary_search(list, n)
        if result != -1:
            print("THE ROLL.NO YOU ENTERED WAS PRESENT FOR THE TRAINING PROGRAM AT POSITION", str(result))
        else:
            print("THE ROLL.NO WAS ABSENT FOR TRAINING PROGRAM")
    if g==2:
        a = fib_search(list,n)
        if a!=-1:
            print("THE ROLL.NO YOU ENTERED WAS PRESENT FOR THE TRAINING PROGRAM AT POSITION",a)
        else:
            print("THE ROLL.NO WAS ABSENT FOR TRAINING PROGRAM")
    if g==3:
        i==1
        break


