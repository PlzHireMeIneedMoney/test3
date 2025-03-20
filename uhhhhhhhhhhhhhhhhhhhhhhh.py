from datetime import datetime
class Person:
    __name:str
    __birthYear:int
    __address:str
    def __init__(self):
        self.__name = ""
        self.__birthYear = 0
        self.__address ="" 
    def __init__(self, __name:str, __birthYear:int, __address:str):
        self.__name = __name
        self.__birthYear = __birthYear
        self.__address = __address
    def Input(self):
        self.__name = input("Input name: ")
        self.__birthYear = input("Input birth year: ")
        self.__address = input("Input address")
    def GetAge(self):
        return datetime.now().year-self.__birthYear
    def ToString(self):
        return f"Person:[{self.__name},Age:{self.GetAge()},Address:{self.__address}"
class Student(Person):
    __program:str
    __year:int
    def __init__(self):
        super().__init__(self.__name,self.__birthYear,self.__address)
        self.__program = ""
        self.__year = 0
    def __init__(self,__name:str,__birthYear:int,__address:int,__program:str,__year:int):
        super().__init__(__name,__birthYear,__address)
        self.__program = __program
        self.__year = __year
    def Input(self):
        super().Input()
        self.__program = input("Input program: ")
        self.__year = input("Input year: ")
    def ToString(self):
        return f"Student[{super().ToString()}- Program:{self.__program},Year:{self.__year}]"
    def ChangeProgram(self,__program:str):
        self.__program = __program
class Staff(Person):
    __department:str
    __salary:float
    def __init__(self):
        super().__init__(self.__name,self.__birthYear,self.__address)
        self.__department=""
        self.__salary=0
    def __init__(self,__name:str,__birthYear:int,__address:str,__department:str,__salary:float):
        super().__init__(self.__name,self.__birthYear,self.__address)
        self.__department = __department
        self.__salary = __salary
    def Input(self):
        super().Input()
        self.__department = input("Input department: ")
        self.__salary = input("Input salary: ")
    def ToString(self):
        return f"Staff[{super().ToString()} - Deparrment:{self.__department},Salary:{self.__salary}]"
    def UpdateSalary(self,__salary:float):
        self.__salary = __salary
StudentA = Student("Wou Yan",2006,"AAA","Mathematics",2024)
print(StudentA.ToString())