import lib.db as db
import lib.pw as pw

class Main():
    def __init__(self):
        self.finished = False;
        self.choice = None;

    def addAccount(self):
        #Checking/Creating user database
        db.createDB();

        # Getting the user's info
        webname = input("Enter website name: ");
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
    def errorStatement(self):
        print("Sorry. Something went wrong. Please try again or reach out to the developer.");
    def viewInfo(self):
        webName = input("Please input the website name (ex: google.com): ");
        db.getInfo(webName);
    def deleteInfo(self):
        webName = input("Please enter website name you would like to delete (ex: google.com): ")
        db.deleteInfo(webName);

    def run(self):
        while (not self.finished):
            print("Please select one of the following options:\n");
            print("1. Create/Add account");
            print("2. Get information");
            print("3. Delete account");
            print("4. Exit");
            try:
                self.choice = input();
                self.choice = int(self.choice);
                if (self.choice > 4 or self.choice < 1):
                    print("Error. Please input a valid number.");
                else:
                    pass;
            except:
                print("Error. Please input a valid number.");
            
            if (self.choice == 1):
                try:
                    self.choice = input("Are you sure you want to add a new account? Y or N: ");
                    if (self.choice == 'Y' or self.choice == 'y'):
                        self.addAccount();
                    else:
                        print("Returning to home screen.")
                        pass;
                except:
                    self.errorStatement();

            elif (self.choice == 2):
                try:
                    self.choice = input("Are you sure you want to view info? Y or N: ");
                    if (self.choice == 'Y' or self.choice == 'y'):
                        self.viewInfo();
                    else:
                        print("Returning to home screen.")
                        pass;
                    
                except:
                    self.errorStatement();

            elif (self.choice == 3):
                try:
                    self.choice = input("Are you sure you want to view info? Y or N: ");
                    if (self.choice == 'Y' or self.choice == 'y'):
                        self.deleteInfo();
                    else:
                        print("Returning to home screen.")
                except:
                    self.errorStatement();
            elif (self.choice == 4):
                return;

main = Main();
main.run();