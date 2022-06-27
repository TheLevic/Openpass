import sqlite3
import os
import PySimpleGUI as sg


filepath = r"";

# Creating the sqlite database
def createDB():
    global filepath;


    try:
        with open ("filepath.txt", "r") as f:
            filepath = f.readline();
    except:
        pass;


    if os.path.exists(filepath):
        return True;
    else:
        try:
            sg.Popup("You have not created a database. Creating now.")
            path = sg.PopupGetFolder("Please enter the desired filepath for your database: ")
            filename = "/" + sg.PopupGetText("Please enter desired database name");
            filepath = path + filename;
            connection = sqlite3.connect(filepath);
            cursor = connection.cursor();
            cursor.execute("CREATE TABLE userinfo (website TEXT, username TEXT, password TEXT)");
            connection.close();
            with open("filepath.txt", "w") as f:
                f.write(filepath);
                f.close();
            return True;
        except:
            sg.PopupError("Error creating database.")
            return False;

# Adding information to database
def addToDB(website, username, password):
    if(createDB()):
        try:
            connection = sqlite3.connect(filepath);
            cursor = connection.cursor();
            cursor.execute("insert into userinfo (website, username, password) values (?, ?, ?)",(website, username, password));
            connection.commit();
            connection.close();
            return True;
        except:
            sg.popup_error("Couldn't connect to database.");
            return False;
    else:
        pass;
        


#Getting information based on the website name
def getInfo(websiteName):
    if (createDB()):
        try:
            connection = sqlite3.connect(filepath);
            cursor = connection.cursor();
            selectQuery = """select * from userinfo where website = ?""";
            cursor.execute(selectQuery,(websiteName,));
            record = cursor.fetchall();
            cursor.close();
            connection.close();
            return record;
        except:
            sg.popup_error("Couldn't retrieve the information. Please try again.");
            return False;
    else:
        sg.PopupError("You had no database for information. Database has now been created. Please try again.");

def deleteInfo(websiteName, username):
    if (createDB()):
        try:
            connection = sqlite3.connect(filepath);
            cursor = connection.cursor();
            deleteQuery = """delete from userinfo where website = ? AND username = ?""";
            cursor.execute(deleteQuery,(websiteName, username));
            connection.commit();
            cursor.close();
            connection.close();
        except:
            sg.popup_error("Couldn't delete the information. Please try again.")
    else:
        sg.PopupError("You had no database for information. Database has now been created. Please try again.")