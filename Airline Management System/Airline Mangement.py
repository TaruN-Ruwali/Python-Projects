print('''==============================================================================================
                                            AIR INDIA''')
print('''                                    WELCOME TO AIRLINE MANAGEMENT
==============================================================================================''')
import os
import pickle

def checklist(num,list):
    if num in list:
        return True
    else:
        return False
''''''

                                             # FUNCTIONS
                                  #FUNCTIONS FOR EDITING AND ADDING RECORDS

def add_pass():
    pf=open("Passenger.dat","ab")
    pr={}
    ask=int(input("Enter the number of records you want to enter:"))
    for i in range(0,ask):
        while True:
            tno=int(input("Enter Ticket number of Passenger:"))
            ch=list(pr.values())
            if checklist(tno,ch):
                print("Ticket number already exists!")
                pass
            else:
                pr["Tcno"]=tno
                break
        pr["Name"]=input("Enter name of Passenger:")
        while True:
            an=int(input("Enter Aadhar card number of Passenger:"))
            if len(str(an))==12:
                while True:
                    ch=list(pr.values())
                    if checklist(an,ch):
                        print("Aadhar number already exists!")
                        pass
                    else:
                        pr["Aadhar"]=an
                        break
                break
            elif len(str(an))<12:
                print("Aadhar number cannot be smaller than 12 digits!")
                pass
            elif len(str(an))>12:
                print("Aadhar number cannot be longer than 12 digits!")
                pass
        while True:    
            mn=int(input("Enter Mobile number of Passenger:"))
            if len(str(mn))==10:
                while True:
                    ch=list(pr.values())
                    if checklist(mn,ch):
                        print("Aadhar number already exists!")
                        pass
                    else:
                        pr["Mobile"]=mn
                        break
                break
            elif len(str(mn))<10:
                print("Mobile number cannot be smaller than 10 digits!")
                pass
            elif len(str(mn))>10:
                print("Mobile number cannot be longer than 10 digits")
        pr["Address"]=input("Enter address of Passenger:")
        pr["Arno"]=input("Enter seat number of Passenger:")
        pickle.dump(pr,pf)
    pf.close()

                                        # FUNCTION FOR VIEWING THE RECORDS

def view_pass():
    pf=open("Passenger.dat","rb")
    try:
        while True:
            pr=pickle.load(pf)
            print("The Passenger details are:")
            print("Ticket number:",pr["Tcno"])
            print("Name:",pr["Name"])
            print("Aadhar number:",pr["Aadhar"])
            print("Mobile number:",pr["Mobile"])
            print("Address:",pr["Address"])
            print("Seat number:",pr["Arno"])
    except EOFError:
        print("number details found! The record is empty!")
    pf.close()

                                        #  FUNCTION FOR SEARCHING A RECORD

def search_pass():
    pf=open("Passenger.dat","rb")
    pr={}
    s=int(input("Enter ticket number of the Passenger to be found:"))
    found=0
    try:
        while True:
            pr=pickle.load(pf)
            if pr["Tcno"]==s:
                print("Found the Passenger!")
                print("Ticket number:",pr["Tcno"])
                print("Name:",pr["Name"])
                print("Aadhar number:",pr["Aadhar"])
                print("Mobile number:",pr["Mobile"])
                print("Address:",pr["Address"])
                print("Seat number:",pr["Arno"])
                found=1
    except EOFError:
        pass
    if found==0:
        print("Invalid ticket number")
    pf.close()

                                        #  FUNCTION FOR DELETING RECORDS

def del_pass():
    pf=open("Passenger.dat","rb")
    t=open("temp.dat","wb")
    pr={}
    s=int(input("Enter ticket number of the Passenger to be removed from the record:"))
    found=0
    try:
        while True:
            pr=pickle.load(pf)
            if pr["Tcno"]==s:
                print("The Passenger details will be removed")
                found=1
            else:
                pickle.dump(pr,t)
    except EOFError:
        pass
    if found==0:
        print("Invalid ticket number")
    pf.close()
    t.close()
    os.remove("Passenger.dat")
    os.rename("temp.dat","Passenger.dat")

                                        # FUNCTION FOR MODIFYING RECORDS

def mod_pass():
    pf=open("Passenger.dat","rb")
    t=open("temp.dat","wb")
    pr={}
    s=int(input("Enter ticket number of the Passenger to be modified:"))
    found=0
    try:
        while True:
            pr=pickle.load(pf)
            if pr["Tcno"]==s:
                pr["Tcno"]=int(input("Enter new ticket number:"))
                pr["Name"]=input("Enter new name:")
                pr["Aadhar"]=int(input("Enter new Aadhar number:"))
                pr["Mobile"]=int(input("Enter new Mobile number:"))
                pr["Address"]=input("Enter new Address:")
                pr["Arno"]=input("Enter new Seat number:")
                found=1
            pickle.dump(pr,t)
    except EOFError:
        pass
    pf.close()
    t.close()
    os.remove("Passenger.dat")
    os.rename("temp.dat","Passenger.dat")   

                                        #FUNCTIONS FOR ADDING AIRPLANE DETAILS

def add_airplane():
     tf=open("airplane.dat","ab")
     tr={}
     ask='y'
     while ask=='y':
         tr["Arno"]=input("Enter airplane number:")
         tr["Name"]=input("Enter name of airplane:")
         tr["Route"]=input("Enter the route of the airplane:")
         tr["Ar_time"]=input("Enter the arrival time of the airplane:")
         tr["Dp_time"]=input("Enter the departure time of the airplane:") 
         tr["Cap"]=int(input("Enter the capacity of the airplane:"))
         pickle.dump(tr,tf)
         ask=input("Do you want to add more records?")
     tf.close()

                                        # FUNCTION FOR VIEWING AIRPLANE DETAILS

def view_airplane():
    tf=open("airplane.dat","rb")
    try:
        while True:
            tr=pickle.load(tf)
            print("The airplane details are:")
            print("airplane number:",tr["Arno"])
            print("Name:",tr["Name"])
            print("Route of the airplane:",tr["Route"])
            print("Arrival time:",tr["Ar_time"])
            print("Departure time:",tr["Dp_time"])
            print("Capacity of the airplane:",tr["Cap"])
    except EOFError:
        print("number details found! The record is empty!")
    tf.close()

                                        #FUNCTION FOR SEARCHING AIRPLANE DETAILS

def search_airplane():
    tf=open("airplane.dat","rb")
    tr={}
    s=input("Enter airplane number to be found:")
    found=0
    try:
        while True:
            tr=pickle.load(tf)
            if tr["Arno"]==s:
                print("Found the airplane!")
                print("airplane number:",tr["Arno"])
                print("Name of the airplane:",tr["Name"])
                print("Route of the airplane:",tr["Route"])
                print("Arrival time:",tr["Ar_time"])
                print("Departure time:",tr["Dp_time"])
                print("Capacity of the airplane:",tr["Cap"])
                found=1
    except EOFError:
        pass
    if found==0:
        print("Invalid airplane number")
    tf.close()

                                        # FUNCTION FOR DELETING PLANE RECORDS

def del_airplane():
    tf=open("airplane.dat","rb")
    t=open("temp.dat","wb")
    tr={}
    s=input("Enter airplane number to be removed from the record:")
    found=0
    try:
        while True:
            tr=pickle.load(tf)
            if tr["Arno"]==s:
                print("The airplane details will be removed!")
                found=1
            else:
                pickle.dump(tr,t)
    except EOFError:
        pass
    if found==0:
        print("Invalid airplane number")
    tf.close()
    t.close()
    os.remove("airplane.dat")
    os.rename("temp.dat","airplane.dat")

                                        # FUNCTION FOR MODIFING AIRPLANE RECORDS

def mod_airplane():
    tf=open("airplane.dat","rb")
    t=open("temp.dat","wb")
    tr={}
    s=input("Enter airplane number to be modified:")
    found=0
    try:
        while True:
            tr=pickle.load(tf)
            if tr["Arno"]==s:
                tr["Arno"]=int(input("Enter new airplane number:"))
                tr["Name"]=input("Enter new name:")
                tr["Route"]=input("Enter new route of the airplane:")
                tr["Ar_time"]=input("Enter new arrival time of the airplane:")
                tr["Dp_time"]=input("Enter new departure time of the airplane:")
                tr["Cap"]=int(input("Enter new capacity of the airplane:"))
                found=1
            pickle.dump(tr,t)
    except EOFError:
        pass
    tf.close()
    t.close()
    os.remove("airplane.dat")
    os.rename("temp.dat","airplane.dat")


                                        #SCHEDULE LOG MENU
                                        #FUNCTIONS FOR EDITING THE SCHEDULE

def add_Sched():
    sf=open("schedule.dat","ab")
    sr={}
    ask='y'
    while ask=='y':
         sr["Arno"]=input("Enter airplane number:")
         sr["Name"]=input("Enter name of airplane:")
         sr["A1_date"]=input("Enter the date of arrival at airport 1:")
         sr["A2_date"]=input("Enter the date of arrival at airport 2:")
         sr["Ar1_time"]=input("Enter the arrival time of the airplane at airport 1:")
         sr["Dp_time"]=input("Enter the departure time of the airplane:")
         sr["Ar2_time"]=input("Enter the arrival time of the airplane at airport 2:")
         sr["Pass"]=int(input("Enter the number of passengers boarding the airplane:"))
         pickle.dump(sr,sf)
    ask=input("Do you want to add more records?")
    sf.close()

                                        #FUNCTION FOR VIEWING SCHEDULE 

def view_Sched():
    sf=open("schedule.dat","rb")
    try:
        while True:
            sr=pickle.load(sf)
            print("The airplane details are:")
            print("Airplane number:",sr["Arno"])
            print("Name:",sr["Name"])
            print("Date of arrival at airport 1:",sr["A1_date"])
            print("Date of arrival at airport 2:",sr["A2_date"])
            print("Arrival time at airport 1:",sr["Ar1_time"])
            print("Departure time:",sr["Dp_time"])
            print("Arrival time at airport 2:",sr["Ar2_time"])
            print("Number of passengers boarding the airplane:",sr["Pass"])
    except EOFError:
        pass
    sf.close()

                                        #FUNCTION FOR SEARCHING SCHEDULE 

def search_Sched():
    sf=open("schedule.dat","rb")
    sr={}
    s=input("Enter airplane number to be found:")
    found=0
    try:
        while True:
            sr=pickle.load(sf)
            if sr["Arno"]==s:
                print("Found the airplane!")
                print("airplane number:",sr["Arno"])
                print("Name:",sr["Name"])
                print("Date of arrival at airport 1:",sr["A1_date"])
                print("Date of arrival at airport 2:",sr["A2_date"])
                print("Arrival time at airport 1:",sr["Ar1_time"])
                print("Departure time:",sr["Dp_time"])
                print("Arrival time at airport 2:",sr["Ar2_time"])
                print("Number of passengers board the airplane:",sr["Pass"])
                found=1
    except EOFError:
        pass
    if found==0:
        print("Invalid airplane number")
    sf.close()

                                        # FUNCION FOR DELETING SCHEDULE

def del_Sched():
    sf=open("schedule.dat","rb")
    t=open("temp.dat","wb")
    lr={}
    s=input("Enter airplane number to be removed from the record:")
    found=0
    try:
        while True:
            sr=pickle.load(sf)
            if sr["Arno"]==s:
                print("The airplane details will be removed!")
                found=1
            else:
                pickle.dump(sr,t)
    except EOFError:
        pass
    if found==0:
        print("Invalid airplane number")
    sf.close()
    t.close()
    os.remove("schedule.dat")
    os.rename("temp.dat","schedule.dat")

                                        # FUNCTION FOR MODIFYING SCHEDULE

def mod_Sched():
    sf=open("schedule.dat","rb")
    t=open("temp.dat","wb")
    sr={}
    s=input("Enter airplane number to be modified:")
    found=0
    try:
        while True:
            sr=pickle.load(sf)
            if sr["Arno"]==s:
                sr["Arno"]=int(input("Enter new airplane number:"))
                sr["Name"]=input("Enter new name:")
                sr["Route"]=input("Enter new route of the airplane:")
                sr["Ar1_time"]=input("Enter new arrival time of the airplane at the first airport:")
                sr["Dp_time"]=input("Enter new departure time of the airplane:")
                sr["Ar2_time"]=input("Enter new arrival time of the airplane at the second airport:")
                sr["pass"]=int(input("Enter new number of passengers broad the airplane:"))
                found=1
            pickle.dump(sr,t)
    except EOFError:
        pass
    sf.close()
    t.close()
    os.remove("schedule.dat")
    os.rename("temp.dat","schedule.dat")

ans='y'
while ans=='y':
    print("Select the menu you want to access:\n1->PASSENGERS DETAILS MENU\n2->AIRPLANE DETAILS MENU\n3->SCHEDULE MENU\n4->EXIT")
    a=int(input("Enter your choice->"))
    if a==1:
       p='y'
       while p=='y':
        print("1:ADD PASSENGER RECORDS\n2:VIEW PASSNGER RECORD\n3:SEARCH PASSENGER RECORDS\n4:DELETE PASSENGER RECORDS\n5:MODIFY PASSENGER RECORDS\nPRESS ANY OTHER NUMBER TO ABORT.")
        z=int(input("Enter your operation:"))
        if z==1:
            add_pass()
        elif z==2:
            view_pass()
        elif z==3:
            search_pass()
        elif z==4:
            del_pass()
        elif z==5:
            mod_pass()
        else:
            break
        p=input("DO YOU WANT TO CONTINUE? PRESS Y TO RETURN TO THE PASSENGER MENU AND ANY OTHER NUMBER TO ABORT.")
    elif a==2:
        q='y'
        while q=='y':
            print("1:ADD AIRPLANE RECORDS\n2:VIEW AIRPLANE RECORD\n3:SEARCH AIRPLANE RECORDS\n4:DELETE AIRPLANE RECORDS\n5:MODIFY AIRPLANE RECORDS\nPRESS ANY OTHER NUMBER TO ABORT.")
            x=int(input("Enter your operation:"))
            if x==1:
                add_airplane()
            elif x==2:
                view_airplane()
            elif x==3:
                search_airplane()
            elif x==4:
                del_airplane()
            elif x==5:
                mod_airplane()
            else:
             break
            p=input("DO YOU WANT TO CONTINUE? PRESS Y TO RETURN TO THE AIRPLANE MENU AND ANY OTHER NUMBER TO ABORT.")
    elif a==3:
        r='y'
        while r=='y':
            print("1:ADD SCHEDULE LOG\n2:VIEW SCHEDULE LOG\n3:SEARCH SCHEDULE LOG\n4:DELETE SCHEDULE LOG\n5:MODIFY SCHEDULE LOG\nPRESS ANY OTHER NUMBER TO ABORT.")
            x=int(input("Enter your operation:"))
            if x==1:
                add_Sched()
            elif x==2:
                view_Sched()
            elif x==3:
                search_Sched()
            elif x==4:
                del_Sched()
            elif x==5:
                mod_Sched()
            else:
             break
            p=input("DO YOU WANT TO ADD MORE RECORDS? PRESS Y TO ACCEPT AND ANY OTHER NUMBER TO ABORT.")
    elif a==4:
        break
    ans=input("ARE YOU SURE YOU WANT TO EXIT? PRESS Y TO RETURN TO MAIN MENU AND ANY OTHER ALPHABET TO QUIT:")



    