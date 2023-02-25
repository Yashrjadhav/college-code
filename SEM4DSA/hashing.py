class imp:
  
    def func1(self):
        self.list1=[]
        self.a=int(input("enter the size of array"))
        for i in range(self.a):
            m=int(input("enter the nos"))
            self.list1.append(m)
            print("array is ",self.list1)
            
    def withoutcollision(self):
        self.list2=[]
        f=int(input("enter the size of hashing table"))
        for i in range(f):
            self.list2.append(0)
        print("hashtable is",self.list2)
        for j in range(len(self.list1)):
            g=self.list1[j]%f
            self.list2[g]=self.list1[j]
        print("output is",self.list2)
        
    def withcollision(self):
        self.list3 = []
        f1 = int(input("enter the size of hashing table"))
        for i in range(f1):
            self.list3.append(0)
        print("hashtable is", self.list3)
        for j in range(len(self.list1)):
            g1=self.list1[j]%f1
            while(self.list3[g1]!=0):
                g1=(g1+1)
            self.list3[g1] = self.list1[j]
        print("hashtable is", self.list3)

r=imp()
r.func1()
r.withoutcollision()
r.withcollision()




