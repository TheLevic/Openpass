import secrets
import string

#Global variables
specialChars = "!@#$%^&*";
alphabet = specialChars + string.ascii_letters + string.digits;


# Generating a secure password the user likes
def generateSecurePassword(length):
    likePW = False;
    while (likePW == False):
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        print("Your password is: " + password);
        t_or_f = input("Do you like your password? Y or N: ");
        if(t_or_f == "y" or t_or_f == "Y"):
            return password
            likePW = True;
        else:
            pass;
    
    