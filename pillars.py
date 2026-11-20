class A:               #single level inheritance
    a=10
class B(A):
    b=20
ob1=B()
print(ob1.a,ob1.b)

class Bank:              #example program for single level inheritance
    bname = 'SBI'
    blac = 'RM nagar'

    def __init__(self, name, phno, eid):
        self.name = name
        self.phno = phno
        self.eid = eid

    def display(self):
        print(self.name, self.phno, self.eid)


class Bank_details(Bank):
    founder = 'deepu'

    def __init__(self, name, phno, eid, add, pan):
        super().__init__(name, phno, eid)
        self.add = add
        self.pan = pan

    def display(self):
        super().display()
        print(self.add, self.pan, self.founder)


c1 = Bank_details(
    'chandana', 9123456789, 'chandana@gmail.com', 'asdfgh', 'ssfff23454'
)
c1.display()

class A:               #multi level inheritance
    a=10
class B(A):
    b=20
class C():
    c=30
class D(C):
    d=40
ob1=D()
print(ob1.c,ob1.d)

class School:          #example program for multi level inheritance
    sname='GPLS'
    sloc='E.city'

class College(School):
    cname='ABC'
    cloc='hoodi'

class Masters(College):
    uname='jain'
    uloc='BSVN'

    @classmethod
    def display(cls):
        print(cls.sname,cls.sloc,cls.cname,cls.cloc,cls.uname,cls.uloc)
Masters.display()

class School:          #example program for heirarchical inheritance
    sname='GPLS'
    sloc='E.city'

class College(School):
    cname='ABC'
    cloc='hoodi'
s1=College()
print(s1.sname)
class Masters(School):
    uname='jain'
    uloc='BSVN'
s2=Masters()
print(School.uname)

class Person:
    def details(self):
        print("Person details")

class Employee(Person):
    def employee(self):
        super().details()
        print("Employee ID: 101")

class Department:
    def department(self):
        print("Department: IT")

class Manager(Employee, Department):
    def manager(self):
        super().employee()
        super().department()
        print("Role: Manager")

obj = Manager()
obj.manager()

class demo:                                    #method overloading
    @staticmethod
    def sam():
        print("Why are you coming late")
    a=sam()
    @staticmethod
    def sam(a,b):
        print(a+b)
    b=sam
    @staticmethod
    def sam(a,b,c):
        print(a*b*c)
    c=sam
ob=demo()
ob.a
ob.b(10,20)
ob.c(1,2,3)

class demo:                           #operator overloading
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return demo(self.value + other.value)
a=demo(100)
b=demo(200)

c=a+b
print(c.value)

print("~~~~~~~~~~~conactenation~~~~~~~~~~")
s1=demo("hi")
s2=demo("good morning")
result=s1+s2
print(result.value)
print(type(result.value))

class Bank:
    __deposite=1000000000
    def __init__(self,name,phone,acno):
        self.name=name
        self.phone=phone
        self.__acno=acno
b=Bank("raju",9876543211,9234567881)
print(b.name)
print(b._Bank__acno)            #syntax to access private members
print(b._Bank__deposite)        ##(onj._classname__var/method)
print(Bank._Bank__deposite)     ##(cname._cname__var/method)
Bank._Bank__deposite=200000000000
print(b._Bank__deposite)

class bank:
    def __init__(self,name,bal):
        self.name=name
        self.__bal=bal
    def get_bal(self,):
        return self.__bal
    def set_bal(self,amount):
        self.__bal=amount
    
    ##deposit
    
    def deposit(self,amount):
        self.set_bal(self.get_bal() + amount)
        
    ##withdraw
    
    def withdraw(self,amount):
        if amount<=self.get_bal():
            self.set_bal(self.get_bal()-amount)
            print("withdrwan successful", amount)
        else:
            print("Insufficient balence")
b=bank("bindu",1000)
print("------before------")
print(b.get_bal())
print("------after-------")

b.deposit(500)
print(b.get_bal())

print("------after withdrwan--------")
b.withdraw(200)
print(b.get_bal())

from abc import ABC,abstractmethod

class student(ABC):
    def __init__(self,name):
        self.name=name
        @abstractmethod
        def study(self):
            pass
        @abstractmethod
        def write(self):
            pass
class school(student):
    def study(self):
        print(self.name,"studying")
    def write(self):
        print(self.name,"writing")
s1=school("raju")
s2=school("kira")
s1.study()
s2.study()