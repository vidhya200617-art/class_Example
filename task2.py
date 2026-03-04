class Member:
  def __init__(self,name,membershipID):
    self.name=name
    self.membershipID=membershipID
  def display(self):
    print("Name:",self.name)
    print("Membership Id:",self.membershipID)
class RegularMember(Member):
  def __init__(self,name,membershipID):
    super().__init__(name,membershipID)
    self.borrow_limit=3
  def getBorrowLimit(self):
    return self.borrow_limit
  def display(self):
    print("Regular Member:")
    print("Name:",self.name)
    print("Borrowing limit:",self.getBorrowLimit(),"books")
    print("-"*30)
class PremiumMember(Member):
  def __init__(self,name,membershipID):
    super().__init__(name,membershipID)
    self.borrow_limit=10
    self.discount="Discount on membership"
    def display(self):
      print("Member type:premium")
      print("Name:",self.name)
      print("Borrowing limit:",self.getBorrowLimit(),"books")
      print("Additional",self.discount)
      print("-",*30)
def main():
   regular=RegularMember("AAA","01")
   premium=PremiumMember("BBB","02")
   regular.display()
   premium.display()
main()





class Student:
  def __init__(self,name,rollnumber):
    self.name =name
    self.rollnumber=rollnumber
  def display(self):
    print("Name:",self.name)
    print("Roll number:",self.rollnumber)
class Undergraduate(Student):
  def __init__(self,name,rollnumber,m1,m2,m3):
    super().__init__(name,rollnumber)
    self.m1=m1
    self.m2=m2
    self.m3=m3
  def calculateaverage(self):
    return(self.m1+self.m2+self.m3)/3
  def display(self):
    avg=self.calculateaverage()
    print("Undergraduate student")
    print("Name:",self.name)
    print("Average marks:",avg)
    print("-"*30)
class Postgraduate(Student):
  def __init__(self,name,rollnumber,m1,m2,m3,m4):
     super().__init__(name,rollnumber)
     self.m1=m1
     self.m2=m2
     self.m3=m3
     self.m4=m4
  def calculateaverage(self):
    return(self.m1+self.m2+self.m3+self.m4)/4
  def display(self):
    avg=self.calculateaverage()
    print("Postgrraduate student")
    print("Name:",self.name)
    print("Average marks:",avg)
    print("_"*30)
def main():
    ug= Undergraduate("anu",101,85,90,88)
    pg= Postgraduate("rahul",201,75,80,85,90)
    ug.display()
    pg.display()
main()
