a=[]
b=[]
c=[]
d=[]
a3=[]
rows=int(input("ENTER THE NO. OF ROWS"))
col=int(input("ENTER THE NO. OF COLOUMS"))
def read():
    m = []
    for i in range(rows):
        a=[]
        for j in range(col):
            a.append(int(input("ENTER THE ELEMENTS")))
        m.append(a)
    return m
def display(m):
    for i in range(rows):
        for j in range(col):
            print("[", m[i][j], "]", end=" ")
        print("\n")
def addition():
    for i in range(rows):
        c.append([])
        for j in range(col):
            c[i].append(a[i][j]+b[i][j])
    for i in range(rows):
        for j in range(col):
            print("[", c[i][j], "]", end=" ")
        print("\n")
def substraction():
    for i in range(rows):
        d.append([])
        for j in range(col):
            d[i].append(a[i][j]-b[i][j])
    for i in range(rows):
        for j in range(col):
            print("[",d[i][j],"]",end=" ")
        print("\n")
def multiplication(a1,b1):
    ans=[]
    r1=len(a1)
    c2=len(b1[0])
    if len(a1)!=len(b1[0]):
        print("invalid")
    for i in range(r1):
        r=[]
        for j in range(c2):
            r.append(0)
        ans.append(r)
    for i in range(r1):
            for k in range(c2):
                for j in range(c2):
                    ans[i][k]+= a1[i][j] * b1[j][k]
    return ans
def transpose():
    print("THE TRANSPOSE OF THE FIRST MATRIX IS :")
    for i in range(rows):
        for j in range(col):
            print("[", a[j][i], "]", end=" ")
        print("\n")
    print("THE TRANSPOSE OF THE SECOND MATRIX IS :")
    for i in range(rows):
        for j in range(col):
            print("[", b[j][i], "]", end=" ")
        print("\n")
a=read()
print("MATRIX A IS: \n")
display(a)
b=read()
print("MATRIX B IS: \n")
display(b)
while True:
    s=int(input('''ENTER YOUR CHOICE:
    PRESS 1: ADDITION OF THE MATRIX:
    PRESS 2: SUSTRACTION OF THE MATRIX:
    PRESS 3: MULTIPLICATION OF THE MATRIX:
    PRESS 4: TRANSPOSE OF THE MATRIX\n'''))
    if s==1:
        print("***ADDITION OF THE MATRIX IS***\n")
        addition()
    if s==2:
        print("***SUBSTRACTION  OF THE MATRIX IS***\n")
        substraction()
    if s==3:
        print("***MULTIPLICATION OF THE MATRIX IS***\n")
        a3=multiplication(a,b)
        display(a3)
    if s==4:
        transpose()
    j=int(input(('''DO YOU WANT TO ENTER DIFFERENT CHOICE:
          IF YES: ENTER 1
          IF NO : ENTER 0::''')))
    if j!=1:
        break


