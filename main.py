import string
import lib.db as db
import lib.pw as pw

specialChars = "!@#$%^&*";
alphabet = specialChars + string.ascii_letters + string.digits;

def addAccount():
    #Checking/Creating user database
    db.createDB();

    # Getting the user's info
    webname = input("Enter website/ name: ");
    username = input("Enter your username: ");
    pwlen = input("Generating secure password. Input length: ");
    # Needing to make sure that the user input is valid.
    while(not isinstance(pwlen,int)):
        try:
            pwlen = int(pwlen);
        except:
            pwlen = input("Invalid input. Please enter a number: ");
    password = pw.generateSecurePassword(pwlen);
    db.addToDB(webname,username,password);


#Getting the information for the website we are adding
def main():

    finished = False;
    while (not finished):
        print("Please select one of the following options:\n");
        print("1. Create/Add account");
        print("2. Get information");
        print("3. Delete account");

        choice = input()
        #Need to add error checking
        choice = int(choice);

        if (choice == 1):
            addAccount();
        elif (choice == 2):
            webName = input("Please input the website name: ");
            db.getInfo(webName);
        elif (choice == 3):
            webName = input("Please enter website name you would like to delete: ")
            db.deleteInfo(webName);
        else:
            pass
main();