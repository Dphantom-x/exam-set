# SET 2430 - Week 2 Lecture & Review Code
# Prof. Haiying Xiao | Fall 2026

def addNum(num):
    sum=0
    for i in range(num):
        sum=sum+i
    print(sum)

#scores=[100,90]
#scores.append(80)
#scores.remove()

#for i in range(3)
#for i in scores[1:3]

def addNum2(num):
    sum=100
    for i in range(num):
        sum=sum+2
    print(sum)

def someFunction(c,d,a=101,b=102):
    sum=0
    print(a,b,c,d)
    sum=a+b+c+d
    print(sum)
    return sum

    
def addNumVar(*val):
    sum=0
    for i in val:
        sum=sum+i
    print(sum)

def show_D_info(**val):
    for i,j in val.items():
        print('My friend\'s {} is {}'.format(i,j))

#object
            #stu_1={"name":'John Doe','DOB':'2006-03-03','score':[100,99,90]}

#OOP
class Staff:
    company_name='ProgramLab'
    #instance variables
    def __init__(self,pName,pPosition,pPay):
        self.name=pName
        self._position=pPosition
        self.pay=pPay
        print('creating an object')        
    def calPay(self):
        hourly_rate=int(input('Enter the hourly rate for %s:'%(self.name)))
        hours=int(input('Enter the hours %s had worked in the past week:'%(self.name)))
        self.pay=hourly_rate*hours
    def __str__(self):
        return ""
    @property
    def position(self):
        print('Getter method')
        return self._position
    @position.setter
    def position(self,value):
        if value=='Manager' or value=='Intern' or value=='developer':
            self._position=value
        else:
            print('Invalid input, nothing changed')    
        
# Example driver to run and test
if __name__ == '__main__':
    print("--- addNum(5) ---")
    addNum(5)
    print("\n--- addNum2(5) ---")
    addNum2(5)
    print("\n--- someFunction(1, 2) ---")
    someFunction(1, 2)
    print("\n--- addNumVar(1, 2, 3, 4, 5) ---")
    addNumVar(1, 2, 3, 4, 5)
    print("\n--- show_D_info ---")
    show_D_info(phone='123-456-7890', major='Software Engineering')
    print("\n--- Staff Class Demo ---")
    staff1 = Staff('Alice', 'developer', 45)
    print("Initial position:", staff1.position)
    staff1.position = 'Manager'
    print("Updated position:", staff1.position)
    staff1.position = 'CEO' # Rejected!
    print("After invalid change:", staff1.position)
