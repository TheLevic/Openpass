import PySimpleGUI as sg
import db
import pw

sg.theme("Dark Green 4");

# Window to help the user create their account
def createAccountMenu():
    layout = [[sg.Text("Enter the website:"), sg.Input(key="-WEBIN-")],
              [sg.Text("Enter your username:"), sg.Input(key="-USERIN-")],
              [sg.Text("Enter preferred password length:"), sg.In(key="-PWDIN-")],
              [sg.Submit(bind_return_key=True)], [sg.Button("Go Back")]];
    window = sg.Window("Create Account", layout);
    event1, values1 = window.read();
    while True:
        if event1 == "Submit":
            try:
                #Getting my users values from their inputs above based on the keys
                webname = values1["-WEBIN-"];
                user = values1["-USERIN-"];
                pwd = values1["-PWDIN-"];
                try:
                    #Trying to convert the length given into an integer
                    pwdLen = int(pwd);
                    likePw = False;
                    while likePw == False:
                        #Generating the users password.
                        userPWD = pw.generateSecurePassword(pwdLen);
                        #Need to see if they like it or not
                        if (sg.popup_yes_no("You generated password is: " + userPWD +"\n Do you like it?") == "Yes"):
                            if(db.addToDB(webname,user,userPWD)):
                                sg.popup_auto_close("Information has been added.");
                                likePw = True;
                            else:
                                sg.PopupError("Couldn't add information. Please try again.")
                                break;
                    break;
                except:
                    sg.popup_auto_close("Error. Please try again. Make sure you enter a valid number. Ex: 12");
                    break;
            except:
                sg.popup_auto_close("Something went wrong. Please try again.");
                break;
        elif event1 is None:
            break;
        elif event1 == ("Go Back"):
            break;
    window.close();
        
# Window to help user get their information
def getUserInfoMenu():
    layout = [[sg.T("Please eneter the website information you want to retrieve:"), sg.I(key="-WEBIN-"), sg.Submit(bind_return_key=True)], [sg.Button("Go Back")]];
    window = sg.Window("View Your Info", layout);
    
    event2, values2 = window.read();
    while True:
        if event2 == "Submit":
            # Getting user information from database.
            userInfo = db.getInfo(values2["-WEBIN-"]);
            # Making sure that it is a list and no errors occured.
            if (isinstance(userInfo, list)):
                if (len(userInfo) == 0):
                    sg.popup_error("Couldn't find information for this site. Please try again.");
                    break;
                else:
                    displayData(userInfo);
                    break;
            else:
                sg.popup_error("Something went wrong. Please try again.");
                break;
        elif event2 == "Go Back":
            break;
        elif event2 is None:
            break;
    window.close();

#Window to display all of the users information
def displayData(userInfo):
    headings = ["Website", "Username", "Password"];
    data = userInfo;
    layout = [[sg.Table(data,headings=headings,justification="left", key="-TABLE-")], [sg.Exit()]];
    window = sg.Window("View Your Data", layout);
    event3, values3 = window.read();
    while True:
        if event3 == sg.WINDOW_CLOSED:
            break;
        elif event3 == "Exit":
            break;
    window.close();

# Window to help user delete their account.
def deleteUserAccountMenu():
    layout = [[sg.T("Please enter the website name for the site you want to delete: "), sg.I(key="-WIN-")],
              [sg.T("Please enter the username for the site you want to delete: "),sg.I(key="-UIN-")],
              [sg.Submit(), sg.Button("Go Back")]];
    window = sg.Window("Delete Account", layout);
    event4, values4 = window.read();
    while True:
        if event4 == "Submit":
            try:
                webname = values4["-WIN-"];
                username = values4["-UIN-"];
                db.deleteInfo(webname, username);
            except:
                sg.PopupError("Please try again.");
                break;
        elif event4 is None:
            break;
        elif event4 == "Go Back":
            break;
    window.close();


def mainWindow():
    layout = [[sg.Text("Please select one of the following options: ")],
         [sg.Button("Create/Add Account")],
         [sg.Button("Get information")],
         [sg.Button("Delete Account")],
         [sg.Button("Encrypt Database", visible=False)],
         [sg.Button("Exit")]];
    window = sg.Window("OpenPass", layout);

    while True:
        event, values = window.read();
        if event == ("Create/Add Account"):
            createAccountMenu();
        elif event == ("Get information"):
            getUserInfoMenu();
        elif event == ("Delete Account"):
            deleteUserAccountMenu();
        elif event in ("Exit"):
            break;
        elif event is None:
            break;
    window.close();

mainWindow();

