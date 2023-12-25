print('dana')
#comment
a=1+\
2+\
3
print(a)
a=4;b=5;c=6
print(a)
if True:
    print('hi')
else :
    print('bye') 
print(type(a))
b='mom'
print(type(b))
c=(1,2,3)
print(type(c))
d={1:'5','b':6,'c':7}

print(type(d))
print(d[1])
k='dana abdallah'
print(k*2)
l=[1,2,3,4]
l1=[6,7,8,1]
print(l[0]/l1[0])
l1.append(0)
print(l1)
a=1234
print(list(str(a)))
l=[1,2,3,4]
print(tuple(l))
a="{0:b}".format(230)
print(a)
b="{0:b}".format(250)
c=int(a) and int(b) 
print(c)
a=700
b=700
print(a is b)
def printme(a,*tub):
    print('a is',a)
    for i in tub:
        print(i)

printme(1,2,3,4)

l=[19,19,2,1]
def co(ll):
    return ll.count(19)==2 and ll[2]>0

print(co(l))

li=[10,10,10,20,30,50,90,80,80]

def r_duplicate (l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
        else:
            pass
    return l2
print(r_duplicate(li))

print(set(li))

def reverse (ll):
    li=ll[::-1]
    return li

print(reverse(li))

class Student :
    studentNumber=0
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.studentNumber=Student.studentNumber+1
    def displyStudentNo(self):
        print('No of students : ',Student.studentNumber)

    def __del__ (self):
        Student.studentNumber-=1

s1=Student('Ali',25)
s2=Student('Amr',30)
print('Name of first student : ',s1.name)
print('Age of first student : ',s1.age)
print('Name of second student : ',s2.name)
print('Age of second student : ',s2.age)
del s2
s1.displyStudentNo()
a="hello"[0]  
print(a)

        



