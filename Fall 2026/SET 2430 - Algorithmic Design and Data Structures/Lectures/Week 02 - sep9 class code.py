#data types
#number eg. int, float, complex
#boolean
#str
#virable
#how to format string
# operator
laptop_brand='APPLE'
msg='The price of {1:d} laptop is {1:d}, the exchange rate is  euro to {2:4.2f} dollar'.format(laptop_brand,1199,1.2232)
msg='The price of %s laptop is %d, the exchange rate is  euro to %4.2f dollar'%(laptop_brand,1199,1.2232)
#+ / *   % //
print(msg)
#input()
laptop_brand=input('Enter the laptop brand you\'d like to purchase')
if laptop_brand=='HP':
    print('HP')
elif laptop_brand=='APPLE':
    print('APPLE')
else:
    print('Not HP OR APPLE')

try:
    result=100/1
    print('------: ',result)
except:
    print('Error!')
#except:
    
#list
scores=[90,80,100,60,105,94]
print(scores)
print(scores[-2])
for i in scores:
    print(i)
# Practice -- show index number along with the value of a list, apply loop
for i,j in enumerate(scores):
    print(i,j)
stu={'name':'John','birth year':2006, 'scores':[90,80,100,60,105,94],'email':'john@gmail.com'}
print(stu)
print(stu['name'])
for i in stu:
    print(i,stu[i])

for i,j in stu.items():
    print('The {} of the student is {}'.format(i,j))
for i in range(1,10):
    print(i)
for i in scores[1:len(scores):2]:
    print(i)   

#isupper()
#lower()
#remove()
#scores.append('hello')
#replace
#split
# task, define a function that can take a varied number of inputs
def show_msg():
    print('form self defined function show_msg:')

def ifPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        return True
# --------------Thursday----------------------------   
def addNum(num):
    sum=0
    for i in range(num):
        sum=sum+i
    print(sum)

def addNum2(num):
    sum=100
    for i in range(num):
        sum=sum+2
    print(sum)

def someFunction(a=101,b=102):
    print(a,b)

    
def addNumVar(*val):
    sum=0
    for i in val:
        sum=sum+i
    print(sum)

def show_D_info(**val):
    for i,j in val.items():
        print('My friend\'s {} is {}'.format(i))
    
#show_D_info(stu_name='John')


#def showStuInfo(school_name,*full_name, **email_pysicaladdress):

#code camp
#John Doe
#john@gmaillcom
#101 new york

#code camp
#Petter  Potter
#'NA'
#'NA'


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
   @property
   def position(self):
       return self._position
   @position.setter
   def position(self,value):
#       if


       
employee1=Staff('Peter','Intern',0)
#
file=open('test.txt','r')
file.read(2)
file.close
file=open('test.txt','r')
file.readlines()
file.close
file=open('test.txt','r')
flie.read()
file.close
# practice: only read 2 bytes each time, eventually read all from the file

with open('test.txt','r') as file:
    content=file.read(2)
    print(content)


#practice: copy test.txt to testnew.txt


        

    





          
