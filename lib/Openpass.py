import PySimpleGUI as sg
import main
import db
import pw

sg.theme("Dark Green 4");

def createAccountMenu():
    layout = [[sg.Text("Enter the website:"), sg.Input(key="-WEBIN-")],
              [sg.Text("Enter your username:"), sg.Input(key="-USERIN-")],
              [sg.Text("Enter preferred password length:"), sg.In(key="-PWDIN-")],
              [sg.Submit()], [sg.Button("Go Back")]];
    window = sg.Window("Create Account", layout);
    event, values = window.read();
    while True:
        if event == "Submit":
            try:
                #Getting my users values from their inputs above based on the keys
                webname = values["-WEBIN-"];
                user = values["-USERIN-"];
                pwd = values["-PWDIN-"];
                try:
                    #Trying to convert the length given into an integer
                    pwd = int(pwd);
                    #Generating the users password.
                    userPWD = pw.generateSecurePassword(pwd);
                    #Need to see if they like it or not
                    sg.popup("You generated password is: " + userPWD +"\nDo you like it?", button_type=1);
                    db.addToDB(webname,user,userPWD);
                    sg.popup_auto_close("Information has been added.");
                except:
                    sg.popup_auto_close("Error. Please enter a valid number.");
                    break;
            except:
                sg.popup_auto_close("Something went wrong. Please try again.");
                break;
        elif event is None:
            break;
        elif event == ("Go Back"):
            break;
    window.close();
        

def getUserInfoMenu():
    layout = [[sg.T("Please the website information you want to retrieve:"), sg.I(key="-WEBIN-")]];
    window = sg.Window("View your Info", layout);
    event, values = window.read();
    window.close();

def deleteUserAccountMenu():
    layout = [[sg.T("Please the website information you want to retrieve:"), sg.I(key="-WEBIN-")]];
    window = sg.Window("Delete Account", layout);
    event, values = window.read();
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

