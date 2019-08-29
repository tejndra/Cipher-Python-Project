
# coding: utf-8

# In[2]:

import time   #Importing Time Library
import random #Importing Random Library
#|----------------------------------------------------------------------------------------------------------------------------|
#New Fake Name Coding
isalpha=True  
while(isalpha!=False):
	#Taking Input
    first_name1 = str(input("Enter First Name 1: "))
    first_name2 = str(input("Enter First Name 2: "))

    last_name1 = str(input("Enter Last Name 1: "))
    last_name2 = str(input("Enter Last Name 2: "))
    isalpha=False
    #Using isalpha for only alphabets value for name.
    if((first_name1.isalpha()==True) and (first_name2.isalpha()==True) and (last_name1.isalpha()==True) and (last_name2.isalpha()==True)):
        new_first_name1=first_name1[:len(first_name1)//2]
        new_first_name2=first_name2[len(first_name2)//2:]
        
        #final Fake First Name after Splitting 
        new_first_name=new_first_name1+new_first_name2
        
        new_last_name1=last_name1[:len(last_name1)//2]
        new_last_name2=last_name2[len(last_name2)//2:]
        
        #final Fake Last Name after Splitting
        new_last_name=new_last_name1+new_last_name2
        
        print("\n",new_first_name+" "+new_last_name,"\n")
    else:
        print("Please Enter Valid Values")
        
#|----------------------------------------------------------------------------------------------------------------------------|
#New Fake Age Coding

#Taking Input
age_1=int(input("Enter Age 1: "))
#The Age Should be between 1 to 100
if((age_1>0) and (age_1<100)):
    new1_age_1=age_1//10
    new2_age_1=age_1%10
else:
    print("Invalid")

#Final New Age 1 
new_age_1=new1_age_1+new2_age_1

#Taking Input
age_2=int(input("Enter Age 2: "))
#The Age Should be between 1 to 100
if((age_2>0) and (age_2<100)):
    new1_age_2=age_2//10
    new2_age_2=age_2%10
else:
    print("Invalid")
    
#Final New Age 2
new_age_2=new1_age_2+new2_age_2
#Final Fake New Age
final_new_age=new_age_1+new_age_2


print("\n","New Age: ",final_new_age,"\n")
#For Current Year Taking Input
c_year=int(input("Enter Current Year: "))
final_c_year=c_year-final_new_age
#Random Month and Date Selection
months=random.randint(1,12)

if((months==1) or (months==3) or (months==5) or (months==7) or (months==8) or (months==10) or (months==12)):  #For 31 Days 
    dates=random.randint(1,31)
elif((months==4) or (months==6) or (months==9) or (months==11)):  #For 30 Days
    dates=random.randint(1,30)
elif(months==2):   #For 29 and 28 Days according to Leap and Non Leap Year
    if((c_year/4==0) and (c_year/100==0) and (c_year/400==0)):   #Leap Year Calculation
        dates=random.randint(1,29)
    else:
        dates=random.randint(1,28)

#Final Fake Date Of Birth
print("\n","New Date Of Birth: ",dates,"/",months,"/",final_c_year,"\n")

#|----------------------------------------------------------------------------------------------------------------------------|
#New Fake ID Coding
ids=(str(final_new_age))
while(len(ids)!=10):
    
    new_id_1=(int(ids))//10
    new_id_2=(int(ids))%10
    new_id=new_id_1+new_id_2
    news_id=new_id%10
    ids=str(ids) + str(news_id)

#Final Fake ID
print("New Id: ",ids,"\n")


#|----------------------------------------------------------------------------------------------------------------------------|
#Cyher Coding
author=[]
firstt=[]
lastt=[]
authorcypher="AuthorisedByNatalieFeng"
firstcypher=new_first_name.lower()  #Changing alphabets to lowercase
lastcypher=new_last_name.lower()    #Changing alphabets to lowercase
authorcyphers=authorcypher.lower()  #Changing alphabets to lowercase
for i in authorcyphers:
    author.append(i)
for ii in firstcypher:    
    firstt.append(ii)
for iii in lastcypher:
    lastt.append(iii)
    
    
#Random Module used here
r1=random.randint(1,10)
r2=random.randint(-10,-1)
r3=random.randint(1,10)
r4=random.randint(-10,-1)
r5=random.randint(1,10)
r6=random.randint(-10,-1)

#I'm making 3 cyphers together which have different random numbers so that it is more difficult to crack.
cypher1 = ''
cypher2 = ''
cypher3 = ''

for x in author:
    authorcyphers=(ord(x))
    if((authorcyphers>=97) and (authorcyphers<=122)):
        cypherr=chr(ord(x)+r1)  #if its between 97 and 122 then r1 will use means +(1 to 10)
        changetoodr=(ord(cypherr))
        if(changetoodr>122):
            cypherr=chr(ord(x)+r2)  #if its more then 122 then r2 will use means -(1 to 10)
        cypher1 += cypherr
    else:
        print("Invalid")
    


for xx in firstt:
    firstcypher=(ord(xx))
    if((firstcypher>=97) and (firstcypher<=122)):
        cypherrr=chr(ord(xx)+r3)   #if its between 97 and 122 then r3 will use means +(1 to 10)
        changeetoodr=(ord(cypherrr))
        if(changeetoodr>122):
            cypherrr=chr(ord(xx)+r4)  #if its more then 122 then r4 will use means -(1 to 10)
        cypher2 += cypherrr
    else:
        print("Invalid")
    


for xxx in lastt:
    lastcypher=(ord(xxx))
    if((lastcypher>=97) and (lastcypher<=122)):
        cypherrrr=chr(ord(xxx)+r5)     #if its between 97 and 122 then r5 will use means +(1 to 10)
        changeeetoodr=(ord(cypherrrr))
        if(changeeetoodr>122):
            cypherrrr=chr(ord(xxx)+r6)  #if its more then 122 then r6 will use means -(1 to 10)
        cypher3 += cypherrrr
    else:
        print("Invalid")
    
#Printing Fake Passport Without Encryption
print ("Fake Passport Without Encryption:","\n")
print ("|=======",new_first_name+" "+new_last_name+"\t\t"+ids,"=======|")
print("|=======",dates,"/",months,"/",final_c_year,"       \t\t   =======|")
print("|=======",authorcypher,"        =======|","\n","\n")
#Printing Fake And Encrypted Passport
print ("Fake And Encrypted Passport:","\n")
#Printing all random values of all 3 cypher
print ("Author Cypher:",r1,r2,"|| FirstName Cypher:",r3,r4,"|| LastName Cypher:",r5,r6,"\n")
print ("|=======",cypher2+" "+cypher3+"\t\t"+ids,"=======|")
print("|=======",dates,"/",months,"/",final_c_year,"       \t\t   =======|")
print("|=======",cypher1,"        =======|")

time.sleep(20) #Using Time Library to show output for 20 Seconds in Python Shell