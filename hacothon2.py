import os
import fileinput
def dotate(data,f_donar,f_amount):
    f_donar.append(input("enter the donar name :"))
    f_amount.append(int(input("amount donated :")))
    data.write(str(f_donar[len(f_amount)-1])+" : "+ str(f_amount[len(f_amount)-1])+"\n")
    print("Unique ID is :",(len(f_amount)-1))
    return(data,f_donar,f_amount)
def retrive(data,f_donar,f_amount):
    print("enter the Unque ID the retrive your transaction data:")
    b=int(input())
    if (b<len(f_amount)):
        print("NAME:",f_donar[b])
        print("AMOUNT:",f_amount[b])
    else:
        print("entered ID is does not exist")
def adddata(data,f_donar,f_amount):
    print("enter the Unque ID the edit the transaction data:")
    b=int(input())
    if (b<len(f_amount)):
        print("Enter the amount to be added :")
        c=int(input())
        for line in fileinput.input(data):
            line=line.replace(str(f_donar[len(f_amount)-1])+" : "+ str(f_amount[len(f_amount)-1]),str(f_donar[len(f_amount)-1]+c)+" : "+ str(f_amount[len(f_amount)-1]))
        f_amount[b]=f_amount[b]+c
    else:
        print("entered ID is does not exist")
def retriveall(data,f_donar,f_amount):
    for i in data:
        print(i)
if( __name__ == "__main__"):
    os.chdir("C:\\Users\\91787\\OneDrive\\Desktop\\my programs\\python")
    data=open("Data.txt",'a+')
    print("If admin enter 1 and if user enter 2")
    f_amount=[]
    f_donar=[]
    key=int(input())
    if(key==1):
        passcode=123456789
        print("Enter the Passcode :")
        p=int(input())
        if(p==passcode):
            print("For add a donation entry 1,retrive a data enter 2, adding the amount to data 3,retriving all data 4 ,EXIT 5")
            while(1):
                comand=int(input())
                if(comand==1):
                    dotate(data,f_donar,f_amount)
                elif(comand==2):
                    retrive(data,f_donar,f_amount)
                elif(comand==3):
                    adddata(data,f_donar,f_amount)
                elif(comand==4):
                    retriveall(data,f_donar,f_amount)
                else:
                    break
        else:
            print("------Invalid password-----")
    elif(key==2):
        print("For add a donation entry 1,retrive a data enter 2, adding the amount to data 3,retriving all data 4 ,EXIT 5")
        while(1):
            comand=int(input())
            if(comand==1):
                dotate(data,f_donar,f_amount)
            elif(comand==2):
                retrive(data,f_donar,f_amount)
            elif(comand==3):
                adddata(data,f_donar,f_amount)
            else:
                break
    