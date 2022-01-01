#Declaring constant variables globally
Blooddropfactor = 15
Fluiddropfactor = 20

print ("Welcome")
print ("")

name = input ("Please input your name\n")
print ("Welcome",name)
print ("")

def action():
    exit= input ("Do you want to exit? \n(e)Yes \n(f)No\n")
    if (exit == "f"):
        qestio()
    elif (exit == "e"):
        print ("Thank You for using my app")
        exit()
    else:
        print ("please,select an option")
        return action()

def qestio():
    reason = input("What do you want to calculate \n(a)BMI or \n(b)Drop factor\n")
    if (reason == "a"):

        #Input needed variables
        WT=float(input('input weight in Kg\n'))
        HT=float(input('input height in metres\n'))

        #calculate BMI using inputed variables and standard formula
        BMI=round(WT/(HT**2),1)
        
        print ("Your BMI is", BMI,"kg/m2")

        #Redirect user to action function
        return action()

    else:
        (reason == "b")

        #Collect needed inputs from user
        Vol=int(input('Input Volume of fluid\n'))
        Time=int(input('Input Time in hours\n'))

    #Determine fluid type
    Fluidtype=input ("(c)Blood or \n(d)Fluid\n")

    if (Fluidtype == "c"):

        #calculate drop factor using inputed variables and standard formula
        Dropfactor=round((Vol*Blooddropfactor)/(Time*60), 1)

        print ("Drop Factor is" , Dropfactor,"drops per minute")

        #Redirect user to action function
        return action()

    else:
        (Fluidtype == "d")

        #calculate drop factor using inputed variables and standard formula
        Dropfactor=round((Vol*Fluiddropfactor)/(Time*60), 1) 
    
        print ("Drop Factor is" , Dropfactor,"drops per minuite")

         #Redirect user to action function
        return action()
        
print (qestio())

    
    
                
