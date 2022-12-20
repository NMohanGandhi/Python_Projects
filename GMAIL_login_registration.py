file  =  open("registrations.txt","w")
print("choice1  -   registration",  "choice2  -  login")


choice  =   int(input(" enter your choice number :   "))

def registration():
    print("REGISTER YOUR ACCOUNT ")
    user1  =  input("register your emal_id :   ")
    user2  =  input("set your password for register email_id :   ")
    dic1 = {}
    dic1[user1]  =  user2
    file.write(str(dic1))
    file.write('\n')
    print(dic1)
    file.close()

def login():
    print("    LOGIN YOUR ACCCOUNT   ")
    login_user =   input("login  with your valid emial_id :  ")
    login_pass  =   input("login with your password   ")
    logfile =  open("registrations.txt","r")
    for line in logfile.readlines():
        val = eval(line)#DICTIONARY
        for keys,values in val.items():
            flag  =  False
            if (login_user == keys) and (login_pass  ==  values):
                print("dear user you have succesfully login ")
                flag  =  True
                break
            else :
                flag = False
        if flag == False:
            print("invalid username/password,kindly register if you are a new user")
        file.close
if choice == 1:
    registration()
    user_input = input("do you want to login (yes/no)")
    if user_input == "yes":
        login()
    else:
        print("thank you for registration ,you have sucessfully registered")
else:
    login()
            

     
   
    
    
    
    
    

