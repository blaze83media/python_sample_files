#python data types
vComplex=2j
vlist=['Ken','Maro','Vobo']
print(vlist[1],len(vlist))

vlist.append('Dafe') #add
print(vlist)

vlist.pop(1)  #delete
print(vlist)


vtuple=('Ken','Maro','Vobo')
vrange=range(12)   
vdict={'fname':'Maro','lname':'Obuks','DOB':'310117'}
vset={'Ken','Maro','Vobo'}
vfrozenset=({'Ken','Maro','Vobo'})

print(vComplex,vlist,vtuple,vrange,vdict,vset)
##########################################
a1=str('Kelly Price is') 
a2=int(50)
a3=float(12.78)
a4=complex(1j)
b1=list(('list','Maro','Vobo'))
b2=tuple(('tuple','Maro','Vobo','tuple','Maro','Vobo'))
print(len(b2))

b3=dict(xdict='Maro',lname='Obuks',DOB=310117)
vb=b3.get('lname')
print(vb)

b4=set(('set','Maro','Vobo'))
b5=frozenset(('xfrozenset','Maro','Vobo'))
print(a1,a2,a3,a4,b1,b2,b3,vb,b4,b5)
##############################################
'''
num = float("%0.2f" % (float(input("Please input your number: "))))
print(num)

num = 3.65
print("The number is {:.2f}".format(num))
#'The number is 3.65'


num = input("Please input your number: ")
num = float("%0.2f" % (num))
print(num)

'''


#variables###############################
a= 'I am a student' #string
b= ' years old'    #string
c= '56'      #int
#use triple quote
e="""I am a student I am a student  
    I am a student, I am a student
    I am a student, I am a student"""
x=a+c+b
print("Let's meet you: " + x + e) 
print(type(c))

f='He is {} {} and he said {}'
print(f.format(c,b,a))


#### if statement #################################
m=20
n=10
if m<n:
    print("You have £10 left")
elif m==n:
    print('You NEED more cash')
else:
    print("You don't need cash")

####while loop#####################################
i=1
while i<6:
    print(i)
    i+=1
else:
    print('i is no longer less than 6')

#####for loop ##########################################
fruits=['apple','pear','banana','mango']
for frt in fruits:
    if frt == "banana":
        break
    print(frt)
    
for frt2 in fruits:
    if frt2 == "banana":
        continue
    print(frt2)
    

#function###########################################
def myfun(): 
  print("This is function statement: " + c + "years")
  
myfun()  #call function

#global scope function##############################
def kname():
    global t_var
    t_var="This is it"
    
kname()
print(t_var)



#### function with attribute############################
def normName(fname,lname):
    print('My first name is '+fname+ ' and my last name is ' +lname)
    
normName('Kenneth','Bovi')

#### function with attribute############################
def subjName(*subj):
    print("She is best in "+subj[1])
    
subjName('Maths','English','Science','Social Science')


#### function with DEFAULT attribute############################
def defCountry(country='the UK'):
    print('I am travelling to '+country)

defCountry()
defCountry('Spain')

def childName(ch1,ch2,ch3):
    print('His name is '+ch2)
    print(ch1+' is friends with '+ch3)
    
childName(ch1='Manny',ch2='Ekene',ch3='Wak')

#########Lamba accepts many attributes but one expression###############
vm=lambda za,zb,zc: za*zb*zc
print(vm(20,30,10))

##############################
def lambdaTest(n):
    return lambda zw: zw*n

mylambdafun= lambdaTest(34)
print (mylambdafun(10))
##############################





###########CLASSES have _init_() function used to assign values to properties###
class MyClass:
    kx='python class 89'
    
p1=MyClass()
print(p1.kx)

#------------------------------------------------------
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def classfun(self):
        print('Hi, please are you ' + self.name + '?')
        
cp=People('Mark',40)
print(cp.name,cp.age)
cp.classfun()

cp.name='Bimbo'
cp.classfun()
print()


#parent class--------------------------------------------------------------
class WeKnow:
    def __init__(self,name,job):
        self.name=name
        self.job=job
        
    def showknw(self):
        print(self.name,self.job)
                      
        ##child class (inherit class) from parent
class Letsknow(WeKnow):       
    pass  #add pass if the function would be empty
    
showchildclass=Letsknow('Blessed','poet')
showchildclass.showknw()
#-------------------------------------------------------------------------

class WeKnowQ:
    def __init__(self,name1,job1):
        self.name1=name1
        self.job1=job1
        
    def showknwQ(self):
        print(self.name1,self.job1)
                      
        ##child class (inherit class) from parent
class LetsknowQ(WeKnowQ):       
    def __init__(self,name1,job1):
        WeKnowQ.__init__(self,name1,job1)  #inherited class init()
    
showchildclassQ=LetsknowQ('Maro','Niman')
showchildclassQ.showknwQ()

###Class # child class# add property # add method----------------------------------------------------------------------

class WeKnowY:
    def __init__(self,name1,job1):
        self.name1=name1
        self.job1=job1
        
    def showknwY(self):
        print(self.name1,self.job1)
                      
        ##child class (inherit class) from parent
class LetsknowY(WeKnowY):       
    def __init__(self,name1,job1,price):
        super().__init__(name1,job1)  #use super() to inherit class init()
        self.amt = price     #add a property       
    
    def welm(self):          #add a method to child class
        print('Thank you',self.name1,self.amt,' is the price for the ',self.job1)
    
showchildclassY=LetsknowY('Marobb','NimanSUPER','2020')
print(showchildclassY.amt)
showchildclassY.showknwY()
showchildclassY.welm()
#------------------------------------------------------------------------
############### JSON#############################
#####convert json to python (use double quotes)
import json
kjson= '{"fname": "Maro", "lname": "Obuks", "DOB": 310117}'
mkjson=json.loads(kjson)
print(mkjson["lname"])



##### convert python to json#################################
kdict={
     'name':'Sch',
     'age':20,
     'sex':'male',
     'pets':'none',
     'cars':[
       {'fname': 'Maro', 'lname': 'Obuks', 'DOB': 310117},
       {'fname': 'Ken', 'lname': 'Tolu', 'DOB': 'klk'}
     ]
}

print(json.dumps(kdict, indent=4, sort_keys=False))

################################################################
#python 3.6 input

username = input("Please enter your name: ")
print("Your username is: "+username)

################################################################
#Python FILE handling
ty=open("numpy1.py","rt")    #r:read, t:text
print(ty.read(5))      #read line 5
###############################################################

#REQUESTS
import requests
rq=requests.get('https://www.vultr.com/docs/setup-a-non-root-user-with-sudo-access-on-ubuntu')
print(rq.text)


#here are two kinds of magics, line-oriented and cell-oriented. Line magics are prefixed with the % character and work much like OS command-line calls: 
#they get as an argument the rest of the line, where arguments are passed without parentheses or quotes.

# %%, and they are functions that get as an argument not only the rest of the line, 
#but also the lines below it in a separate argument.



###########################################################
##MYSQL DATABASE with python#############################
####  python -m pip install mysql-connector
####  conda install mysql-connector


#########################################################################
#insert into db
'''
import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        user="username",
        passwd="",
        database="db_trend"
        )

mycursor=mydb.cursor()

sql= "INSERT INTO table1 (name,email) VALUES (%s, %s)" #Note that %s is python's escape to stop sql inj
val= ("Blz","blz@blz.com")
mycursor.execute(sql,val) 

mydb.commit()

print(mycursor.rowcount, "Your record was inserted")  #confirmation
print("last insert record ID: ", mycursor.lastrowid)  #get id of last insert data

'''


#########################################################################
#select data from db
'''
import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        user="username",
        passwd="",
        database="db_trend"
        )

mycursor=mydb.cursor()

mycursor.execute("select * FROM table1 WHERE address= %s LIMIT 5 OFFSET 2") #Note that %s is python's escape to stop sql inj
# or use: mycursor.execute("select name, address FROM table1")

myresult= mycursor.fetchall()
# or to fetch one row use:  myresult= mycursor.fetchone()

for x in myresult:
    print(x)

'''

#########################################################################
#delete data
'''
import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        user="username",
        passwd="",
        database="db_trend"
        )

mycursor=mydb.cursor()
sql = "DELETE FROM table1 WHERE address = %s "
adr=("UB98DF",)
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
'''


#########################################################################
#UPDATE data
'''
import mysql.connector

mydb=mysql.connector.connect(
        host="localhost",
        user="username",
        passwd="",
        database="db_trend"
        )

mycursor=mydb.cursor()
sql = "UPDATE table1 SET address = %s WHERE address = %s"
val = ("NW12ED","MK89AL")

mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record(s) updated")
'''