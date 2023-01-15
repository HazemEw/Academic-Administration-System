from Employee import Employee
class Admin(Employee):
    def __init__(self,EmployeeID,Name,DateOfBirth,MaritalStatus,NumberOfChilds,Gender,ContactInformation,Type,Status,Department, StartingTime, BasicSalary, HealthInsurance,Vacation):
        super().__init__(EmployeeID,Name,DateOfBirth,MaritalStatus,NumberOfChilds,Gender,ContactInformation,Type,Status,Department, StartingTime, BasicSalary, HealthInsurance)
        self.Vacation=Vacation

    def setNewVacation(self,NewVacation):
        self.Vacation = NewVacation

    def getVacation(self):
        return self.Vacation

    def AddNewEmployee():
        addEmployee=[]
        printer=["what is employee ID:","what is employee Name:","what is DateOfBirth:","what is MaritalStatus:","what is NumberOfChilds:","what is Gender:","what is ContactInformation:","what is Type:","what is Status:","what is Department:","what is StartingTime:","what is BasicSalary:","what is HealthInsurance:","what is Vacation:"]
        for i in range(14):
            print(printer[i])
            read=input()
            addEmployee.append(read)
        NewEmployeeObject=Admin(addEmployee[0],addEmployee[1],addEmployee[2],addEmployee[3],addEmployee[4],addEmployee[5],addEmployee[6],addEmployee[7],addEmployee[8],addEmployee[9],addEmployee[10],addEmployee[11],addEmployee[12],addEmployee[13])
        return NewEmployeeObject