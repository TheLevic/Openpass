
import secrets
import string
import os.path




#Checking to see if the file exists, or if we need to create a local password file
def checkFile():
    if os.path.exists(r"Your file path goes here"):
        print("File exists")
        return;
    else:
        file = open(r"Your file path goes here",'w');
        print("Making file")
        file.close();

#Generating a secure password that the user likes
def generateSecurePassword(length):
    likePW = False;
    pwlen = int(length);
    while (likePW == False):
        password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(pwlen))
        print("Your password is: " + password);
        t_or_f = input("Do you like your password? Y or N: ");
        if(t_or_f == "y" or t_or_f == "Y"):
            return password
            likePW = True;

        else:
            pass;
    

#Getting the information for the website we are adding
def addInfo():
    #Info stage

    webname = input("Enter website name: ");
    username = input("Enter your username:");
    pwlen = input("Generating secure password. Input length: ");
    password = generateSecurePassword(pwlen);


    #Writing stage

    print("Writing info to file");
    file = open(r"Your file path goes here", "a");
    uname = "Username: " + username + "\n";
    pwd = "Password: " + password + "\n";
    website = "Website: " + webname + "\n";
    
    file.write("----------\n");
    file.write(website);
    file.write(uname);
    file.write(pwd);
    file.write("----------\n");
    file.write("\n");

#Going to add encryption and searching soon.
    
addInfo();