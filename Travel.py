from datetime import datetime
from time import time,ctime
import os
import time

filename=""
ticNo=0
total=0

def time1():
    t=time.time()
    p=datetime.now()
    return str(p)[11:19]

def date1():
    p=datetime.now()
    t=p.strftime("%d-%m-%y")
    return t

def createFile():
    p=date1()+".txt"
    file=open(p,'w')
    file.write("WELCOME TO ASHOK TRAVELS !\nTicket No.\tAmount  \t     Time\n")
    file.close()
    return p

def ticketNumber(fname):
    b=""
    for i in fname:
        if ord(i)>=48 and ord(i)<=57:
            b+=i
    c=b[:-6:-1]
    d=int(b)-int(c)
    return str(d)

def clear():
    os.system("cls")

def book():
    clear()
    print("Select one option\n\n0.  Exit\n1.  Continue\n")
    n=input()
    if n=="0":
        clear()
        structure2()
    elif n=="1":
        clear()
        print("1.Indore\n2.Ujjain\n3.Nagda\n4.Jaora\n5.Mandsour\n6.Nimach\n")
        a=int(input("Enter Source City No.\n"))
        b=int(input("Enter Destination City No.\n"))

        if(a!=b and a,b>=1 and a,b<=6):
            calcTicket(a,b)
            book()
        else:
            print("Invalid Input")
            book()
    else:
        print("Invalid Input")
        book()

def calcTicket(a,b):
    global ticNo
    global total
    r=abs(a-b)*60
    total+=r
    printTicket(ticNo,r)
    ticNo+=4

def printTicket(ticNo,r):
    global filename
    print("\n\n\n\n\t\tYour Ticket Number is ",ticNo)
    print("\t\t Amount",r)
    print("\t\tPlease collect your Ticket Number")
    print("\t\t::::::::::::Thank You::::::::::::")

    p=str(ticNo)+"                               "+str(r)+"                               "+time1()
    writeFile(filename,p)
    input("\n\nPress Enter")

def writeFile(fn,p):
    f=open(fn,'a')
    f.write(p)
    f.write("\n")
    f.close()



def structure1():
    clear()
    print("\t\tPress the Number\n\n1.  Start\n2.  Close\n")
    n=input()
    if n=="1":
        clear()
        structure2()
    elif n=="2":
        pass
        exit
    else:
        print("Invalid Selection")
        input("Press Enter")
        structure1()

def structure2():
    clear()
    global total
    print("Select one option\n\n1.  Book Ticket\n2.  Total collection of the day\n3.  Exit")
    n=input()
    if n=="1":
        p=book()
    elif n=="2":
        pswd=input("Enter the password\n")
        if pswd=="asr12345":
            print("Total Collection of the day is Rs.",total)
            input("Press Enter")
            structure2()
        else:
            print("Incorrect password")
            input("Press Enter")
            structure2()
    elif n=="3":
        structure1()
    else:
        print("Invalid Option")
        input("Press Enter")
        structure2()


def main():
    global filename
    global ticNo
    fl=date1()+".txt"
    if os.path.isfile(fl):
        filename=fl
        pass
    else:
        filename=createFile()
    ticNo=int(ticketNumber(filename))

    structure1()
main()