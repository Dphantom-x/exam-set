
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
        
        #working with file


# -------------------------------------------------------------
# Assignment 2
# -------------------------------------------------------------

# Part A: Prime Number Check
def is_prime(n):
    # check for non-integers (floats, strings, None, booleans)
    if type(n) != int or type(n) == bool:
        return False
    # numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # check factors
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Part B: Remove Adjacent Duplicates
def remove_adjacent_duplicates(id_list):
    res = []
    for id in id_list:
        # if the current id matches the last one added, remove it
        if len(res) > 0 and res[-1] == id:
            res.pop()
        else:
            res.append(id)
    return res

# alias in case the test script calls camelCase
removeAdjacentDuplicates = remove_adjacent_duplicates


# Part C: Display Student Information Using Variable Arguments
def disStuInfo(schoolID, *last_names, **first_name_email):
    last_list = list(last_names)
    email_list = list(first_name_email.items())
    
    # 1. Loop through all provided last names
    for i in range(len(last_list)):
        print(schoolID)
        if i < len(email_list):
            first, email = email_list[i]
            print(last_list[i])
            print(first)
            print(email)
        else:
            print("'unmatched'")
            print(last_list[i])
        print()
        
    # 2. Check any remaining first name and emails without a last name
    for i in range(len(last_list), len(email_list)):
        first, email = email_list[i]
        print(schoolID)
        print("'unmatched'")
        print(first)
        print(email)
        print()


if __name__ == '__main__':
    # Part A test
    print("--- Part A ---")
    print("is_prime(2):", is_prime(2))
    print("is_prime(7):", is_prime(7))
    print("is_prime(4):", is_prime(4))
    print("is_prime(1):", is_prime(1))
    print("is_prime(0):", is_prime(0))
    print("is_prime(-3):", is_prime(-3))
    print("is_prime(2.5):", is_prime(2.5))
    print("is_prime('hello'):", is_prime('hello'))
    print("is_prime(None):", is_prime(None))
    print("is_prime(True):", is_prime(True))

    # Part B test
    print("\n--- Part B ---")
    sample_ids = [1, 2, 2, 3, 3, 3, 4]
    print("Input: ", sample_ids)
    print("Output:", remove_adjacent_duplicates(sample_ids))

    # Part C test
    print("\n--- Part C ---")
    disStuInfo(10001, 'Smith', 'Potter', John='jSmith@gmail.com', Petter="Petter@yahoo.com", JackLast="j@gmail.com")
