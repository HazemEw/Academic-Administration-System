class Employee:
    def __init__(self,EmployeeID,Name,DateOfBirth,MaritalStatus,NumberOfChilds,Gender,ContactInformation,Type,Status,Department, StartingTime, BasicSalary, HealthInsurance):
        self.EmployeeID = EmployeeID
        self.Name = Name
        self.DateOfBirth = DateOfBirth
        self.MaritalStatus = MaritalStatus
        self.NumberOfChilds = NumberOfChilds
        self.Gender = Gender
        self.ContactInformation = ContactInformation
        self.Type = Type
        self.Status = Status
        self.Department = Department
        self.StartingTime = StartingTime
        self.BasicSalary = BasicSalary
        self.HealthInsurance = HealthInsurance

    def setNewEmployeeID(self,NewEmployeeID):
        self.EmployeeID = NewEmployeeID
    def getEmployeeID(self):
        return self.EmployeeID

    def setNewName(self,NewName):
        self.Name = NewName
    def getName(self):
        return self.Name

    def setNewDateOfBirth(self,NewDateOfBirth):
        self.DateOfBirth = NewDateOfBirth
    def getDateOfBirth(self):
        return self.DateOfBirth

    def setNewMaritalStatus(self,NewMaritalStatus):
        self.MaritalStatus = NewMaritalStatus
    def getMaritalStatus(self):
        return self.MaritalStatus

    def setNewNumberOfChilds(self,NewNumberOfChilds):
        self.NumberOfChilds = NewNumberOfChilds
    def getNumberOfChilds(self):
        return self.NumberOfChilds

    def setNewGender(self,NewGender):
        self.Gender = NewGender
    def getGender(self):
        return self.Gender

    def setContactInformation(self,NewContactInformation):
        self.ContactInformation = NewContactInformation
    def getContactInformation(self):
        return self.ContactInformation

    def setNewType(self,NewType):
        self.Type = NewType
    def getType(self):
        return self.Type

    def setNewStatus(self,NewStatus):
        self.Status = NewStatus
    def getStatus(self):
        return self.Status

    def setNewDepartment(self,NewDepartment):
        self.Department = NewDepartment
    def getDepartment(self):
        return self.Department

    def setNewStartingTime(self,NewStartingTime):
        self.StartingTime = NewStartingTime
    def getStartingTime(self):
        return self.StartingTime

    def setNewBasicSalary(self,NewBasicSalary):
        self.BasicSalary = NewBasicSalary
    def getBasicSalary(self):
        return self.BasicSalary

    def setNewHealthInsurance(self,NewHealthInsurance):
        self.HealthInsurance = NewHealthInsurance
    def getHealthInsurance(self):
        return self.HealthInsurance
#--------------------------------------------------------------
    def AddNewEmployee():
        addEmployee=[]
        printer=["what is employee ID:","what is employee Name:","what is DateOfBirth:","what is MaritalStatus:","what is NumberOfChilds:","what is Gender:","what is ContactInformation:","what is Type:","what is Status:","what is Department:","what is StartingTime:","what is BasicSalary:","what is HealthInsurance:"]
        for i in range(13):
            print(printer[i])
            read=input()
            addEmployee.append(read)
        NewEmployeeObject=Employee(addEmployee[0],addEmployee[1],addEmployee[2],addEmployee[3],addEmployee[4],addEmployee[5],addEmployee[6],addEmployee[7],addEmployee[8],addEmployee[9],addEmployee[10],addEmployee[11],addEmployee[12])
        return NewEmployeeObject
#--------------------------------------------------------------





        
