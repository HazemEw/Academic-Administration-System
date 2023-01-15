#welcome in our project()
from Academic import Academic
from Employee import Employee
from Admin import Admin
#------------------------------------------------
print("WELCOME IN EMPLOYEE PROJECT")
while True:
    print("ENTER THE NAME OF THE EMPLOYEE RECORD FILE:")
    nameFile=input()
    if nameFile=="GA.txt":
       fopen= open("GAttributes.txt", "r")
       EmployeeList=[]
       AdminList=[]
       AcademicList=[]
       part=[]
       for general in fopen.readlines():
            part=general.split(';')
            EmployeeObject=Employee(part[0],part[1],part[2],part[3],part[4],part[5],part[6],part[7],part[8],part[9],part[10],part[11],part[12])
            EmployeeList.append(EmployeeObject)
       for i in range(len(EmployeeList)):
            if EmployeeList[i].Type==" Administrative":
                Aopen=open("Administrative.txt","r")
                Year=[]
                VacationDays=[]
                for line in Aopen.readlines():
                    Sline=line.split('; ')
                    if Sline[0]==EmployeeList[i].EmployeeID:
                        Year.append(Sline[1])
                        VacationDays.append(Sline[2].removesuffix('\n'))
                        Vacation = dict(zip(Year,VacationDays))
                AdmnObject=Admin(EmployeeList[i].EmployeeID,EmployeeList[i].Name,EmployeeList[i].DateOfBirth,EmployeeList[i].MaritalStatus,EmployeeList[i].NumberOfChilds,EmployeeList[i].Gender,EmployeeList[i].ContactInformation,EmployeeList[i].Type,EmployeeList[i].Status,EmployeeList[i].Department,EmployeeList[i].StartingTime,EmployeeList[i].BasicSalary,EmployeeList[i].HealthInsurance,Vacation)
                AdminList.append(AdmnObject)
            elif EmployeeList[i].Type==" Academic":
                Aopen=open("Academic.txt","r")
                Year=[]
                Semester=[]
                Year_Semester=[]
                AllCourses=[]
                for line in Aopen.readlines():
                    Sline=line.split('; ')
                    if Sline[0]==EmployeeList[i].EmployeeID:
                        Semester.append(Sline[1])
                        Year.append(Sline[2])
                        AllCourses.append(Sline[3].removesuffix('\n'))
                        for i in range(len(Year)):
                            Year_Semester.append(Year[i]+"-"+Semester[i])
                        Experience = dict(zip(Year_Semester,AllCourses))  
                AcademicObject= Academic(EmployeeList[i].EmployeeID,EmployeeList[i].Name,EmployeeList[i].DateOfBirth,EmployeeList[i].MaritalStatus,EmployeeList[i].NumberOfChilds,EmployeeList[i].Gender,EmployeeList[i].ContactInformation,EmployeeList[i].Type,EmployeeList[i].Status,EmployeeList[i].Department,EmployeeList[i].StartingTime,EmployeeList[i].BasicSalary,EmployeeList[i].HealthInsurance,Experience)
                AcademicList.append(AcademicObject)
       break
    else:
         print("ERORR: FILE NOT FOUND!")
#------------------------------------------------
def Update(Obj,String):
    if String == "EmployeeID":
        print("the new value of employee id:")
        NewValue=input()
        
        EmployeeList[Obj].setNewEmployeeID(NewValue)
    elif String == "Name":
        print("the new value of Name:")
        NewValue=input()
        EmployeeList[Obj].setNewName(NewValue)
    elif String == "DateOfBirth":
        print("the new value of DateOfBirth:")
        NewValue=input()
        EmployeeList[Obj].setNewDateOfBirth(NewValue)
    elif String == "MaritalStatus":
        print("the new value of MaritalStatus:")
        NewValue=input()
        EmployeeList[Obj].setNewMaritalStatus(NewValue)
    elif String == "NumberOfChilds":
        print("the new value of NumberOfChilds:")
        NewValue=input()
        EmployeeList[Obj].setNewNumberOfChilds(NewValue)
    elif String == "Gender":
        print("the new value of Gender:")
        NewValue=input()
        EmployeeList[Obj].setNewGender(NewValue)
    elif String == "ContactInformation":
        print("the new value of ContactInformation:")
        NewValue=input()
        EmployeeList[Obj].setNewContactInformation(NewValue)
    elif String == "Type":
        print("the new value of Type:")
        NewValue=input()
        EmployeeList[Obj].setNewType(NewValue)
    elif String == "Status":
        print("the new value of Status:")
        NewValue=input()
        EmployeeList[Obj].setNewStatus(NewValue)
    elif String == "Department":
        print("the new value of Department:")
        NewValue=input()
        EmployeeList[Obj].setNewDepartment(NewValue)
    elif String == "StartingTime":
        print("the new value of StartingTime:")
        NewValue=input()
        EmployeeList[Obj].setNewStartingTime(NewValue)
    elif String == "BasicSalary":
        print("the new value of BasicSalary:")
        NewValue=input()
        EmployeeList[Obj].setNewBasicSalary(NewValue)
    elif String == "HealthInsurance":
        print("the new value of HealthInsurance:")
        NewValue=input()
        EmployeeList[Obj].setNewHealthInsurance(NewValue)
#------------------------------------------------
def  UpdateGeneralAttributes():
        Attribute=["EmployeeID","Name","DateOfBirth","MaritalStatus","NumberOfChilds","Gender","ContactInformation","Type","Status","Department","StartingTime","BasicSalary","HealthInsurance"]
        print("what is the employee ID:")
        read=input()
        for i in range(len(EmployeeList)):
            if EmployeeList[i].EmployeeID==read:
                ThisEmployee=EmployeeList[i]
                print(ThisEmployee)
                print("what is the attributes:")
                print("[EmployeeID]     [Name]       [DateOfBirth]         [MaritalStatus]")
                print("[NumberOfChilds] [Gender]     [ContactInformation]  [Type]")
                print("[Status]         [Department] [StartingTime]        [BasicSalary]   [HealthInsurance]")
                read=input()
                for j in range(len(Attribute)):
                    if str(read) == Attribute[j]:
                        ThisAttribute=Attribute[j]
                        Update(i,ThisAttribute)
                        print("THE ATTRIBUTE IS CHANGE(^-^)")
#------------------------------------------------
def  UpdateAdminAttributes():
        Attribute=["EmployeeID","Name","DateOfBirth","MaritalStatus","NumberOfChilds","Gender","ContactInformation","Type","Status","Department","StartingTime","BasicSalary","HealthInsurance"]
        print("what is the employee ID:")
        read=input()
        for i in range(len(AdminList)):
            if AdminList[i].EmployeeID==read:
                ThisAdmin=AdminList[i]
                print("what is the attributes:")
                print("[EmployeeID]     [Name]       [DateOfBirth]         [MaritalStatus]")
                print("[NumberOfChilds] [Gender]     [ContactInformation]  [Type]")
                print("[Status]         [Department] [StartingTime]        [BasicSalary]   [HealthInsurance]")
                read=input()
                for j in range(len(Attribute)):
                    if str(read) == Attribute[j]:
                        ThisAttribute=Attribute[j]
                        Update(i,ThisAttribute)
                        print("THE ATTRIBUTE IS CHANGE(^-^)")
                        break
#------------------------------------------------
def UpdateAcademicAttributes():
    print("hello")
#------------------------------------------------
while True:
    print("-----------------------------^_^---------------------------")
    print("1. Add a new employee record")
    print("2. Update general attributes")
    print("3. Add/update administrative employee attribute")
    print("4. Add/update academic employee attribute")
    print("5. Employee’s statistics")
    print("6. Salary statistics")
    print("7. Retirement information")
    print("8. Courses statistics")
    print("9. Administrative employees’ statistics")
    print("10. Academic employees’ statistics")
    print("-----------------------------^_^---------------------------")
    print("ENTER THE NUMBER OF YOUER CHOICE:")
    option=input()
    if option =="1":
        writer=Employee.AddNewEmployee()
        EmployeeList.append(writer)
        WritFile="\n"+str(writer.EmployeeID)+"; "+str(writer.Name)+"; "+str(writer.DateOfBirth)+"; "+str(writer.MaritalStatus)+"; "+str(writer.NumberOfChilds)+"; "+str(writer.Gender)+"; "+str(writer.ContactInformation)+"; "+str(writer.Type)+"; "+str(writer.Status)+"; "+str(writer.Department)+"; "+str(writer.StartingTime)+"; "+str(writer.BasicSalary)+"; "+str(writer.HealthInsurance)
        fopen= open("GAttributes.txt", "a")
        fopen.write(WritFile)
        print("NEW EMPLOYEE HAS BEEN ADDED (^-^)")
    elif option=="2":
        print(EmployeeList[1].EmployeeID)
        UpdateGeneralAttributes()
        break
    elif option=="3":
        print("Chose Add or Update Administrative employee attribute")
        chose=input()
        if str(chose)=="Add":
            writer=Admin.AddNewEmployee()
            AdminList.append(writer)
            WritFileEmployee="\n"+str(writer.EmployeeID)+"; "+str(writer.Name)+"; "+str(writer.DateOfBirth)+"; "+str(writer.MaritalStatus)+"; "+str(writer.NumberOfChilds)+"; "+str(writer.Gender)+"; "+str(writer.ContactInformation)+"; "+str(writer.Type)+"; "+str(writer.Status)+"; "+str(writer.Department)+"; "+str(writer.StartingTime)+"; "+str(writer.BasicSalary)+"; "+str(writer.HealthInsurance)
            WritFileAdmin="\n"+str(writer.EmployeeID)+"; "+str(writer.Vacation)
            fopen= open("GAttributes.txt", "a")
            fopen.write(WritFileEmployee)
            fopen= open("Administrative.txt", "a")
            fopen.write(WritFileAdmin)
        elif str(chose)=="Update":
            print("Hi")
        print("DONE3")
        break
    elif option=="4":
        print("DONE3")
        break
    elif option=="5":
        print("DONE3")
        break
    elif option=="6":
        print("DONE3")
        break
    elif option=="7":
        print("DONE3")
        break
    elif option=="8":
        print("DONE3")
        break
    elif option=="9":
        print("DONE3")
        break
    elif option=="10":
        print("DONE3")
        break
#------------------------------------------------
