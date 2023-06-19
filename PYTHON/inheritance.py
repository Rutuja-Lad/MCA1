#single Inheritance
class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def Display(self):
        print("My name is{}".format(self.name))
        print("My id is{}".format(self.idnumber))
class employee(person):
    def __init__(self,name,idnumber,salary,job):
        self.salary=salary
        self.job=job
        person.__init__(self,name,idnumber)
    def Show(self):
        print("My name is {}".format(self.name))
        print("ID {}".format(self.idnumber))
        print("My job role is {}".format(self.job))
obj1=employee("Rutuja",49,90000,"Developer")   
obj1.Show() 
obj=person("Ram",8)   
obj.Display()

