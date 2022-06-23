import db as db
import pw as pw


def errorStatement():
    print("Sorry. Something went wrong. Please try again or reach out to the developer.");


def viewInfo():
    webName = input("Please input the website name (ex: google.com): ");
    db.getInfo(webName);


def deleteInfo():
    webName = input("Please enter website name you would like to delete (ex: google.com): ")
    db.deleteInfo(webName);

def run():
    finished = False;
    while (not finished):
        print("Please select one of the following options:\n");
        print("1. Create/Add account");
        print("2. Get information");
        print("3. Delete account");
        print("4. Exit");
        try:
            choice = input();
            choice = int(choice);
            if (choice > 4 or choice < 1):
                print("Error. Please input a valid number.");
            else:
                pass;
        except:
            print("Error. Please input a valid number.");
        
        if (choice == 1):
            try:
                choice = input("Are you sure you want to add a new account? Y or N: ");
                if (choice == 'Y' or choice == 'y'):
                    pass;
                else:
                    print("Returning to home screen.")
                    pass;
            except:
                errorStatement();

        elif (choice == 2):
            try:
                choice = input("Are you sure you want to view info? Y or N: ");
                if (choice == 'Y' or choice == 'y'):
                    viewInfo();
                else:
                    print("Returning to home screen.")
                    pass;
                
            except:
                errorStatement();

        elif (choice == 3):
            try:
                choice = input("Are you sure you want to view info? Y or N: ");
                if (choice == 'Y' or choice == 'y'):
                    deleteInfo();
                else:
                    print("Returning to home screen.")
            except:
                errorStatement();
        elif (choice == 4):
            return;