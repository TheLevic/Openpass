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
                self.addAccount();
            elif (self.choice == 2):
                webName = input("Please input the website name (ex: google.com): ");
                db.getInfo(webName);
            elif (self.choice == 3):
                webName = input("Please enter website name you would like to delete (ex: google.com): ")
                db.deleteInfo(webName);
            elif (self.choice == 4):
                return;
            else:
                pass;

main = Main();
main.run();