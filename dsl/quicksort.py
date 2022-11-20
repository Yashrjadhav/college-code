'''Write a Python program to store first year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using quick sort
and display top five scores'''
def quick_sort(arr, low, high):
    if low < high:
        ind = split(arr, low, high)
        quick_sort(arr, low, ind - 1)
        quick_sort(arr, ind + 1, high)

def split(arr, low, high):
    index = low - 1
    for i in range(low, high):
        if arr[i] <= arr[high]:
            index += 1
            arr[i], arr[index] = arr[index], arr[i]
    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return index + 1

def enter_lst():
    n = int(input("ENTER THE TOTAL NUMBER OF STUDENTS:"))
    lst = []
    for i in range(n):
        rollno = float(input("ENTER THE PERCENTAGE OF STUDENTS:"))
        lst.append(rollno)
    print("LIST OF MARKS ENTERED IS:", lst)
    return lst


while True:
    print("ENTER THE OPERATION YOU WANT TO PERFORM:")
    print("1.ENTER A NEW LIST OF STUDENT MARKS:")
    print("2.EXIT CODE:")
    ch = int(input("ENTER YOUR CHOICE:"))
    if ch == 1:
        lst = enter_lst()
        quick_sort(lst, 0, len(lst)-1)
        print("THE HIGHEST 5 SCORES ARE :")
        for i in range(-1, -6, -1):
            print(lst[i])
    elif ch == 2:
        break
    print("-" * 50)
print("CODE EXITED")



