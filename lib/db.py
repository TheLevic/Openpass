import sqlite3
import os
import PySimpleGUI as sg


# Please put desired filepath below, as well as what you would like to name your database file.

filename = "pwmanager";
filepath = r"filepath goes here" + filename;

# Creating the sqlite database
def createDB():
    if os.path.exists(filepath):
        pass;
    else:
        connection = sqlite3.connect(filepath);
        cursor = connection.cursor();
        cursor.execute("CREATE TABLE userinfo (website TEXT, username TEXT, password TEXT)");
        connection.close();

# Adding information to database
def addToDB(website, username, password):
    createDB();
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
        


#Getting information based on the website name
def getInfo(websiteName):
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
        sg.popup_error("Couldn't retrieve the information. Please try again.")
        return False;

def deleteInfo(websiteName):
    connection = sqlite3.connect(filepath);
    cursor = connection.cursor();
    try:
        deleteQuery = """delete from userinfo where website = ?""";
        cursor.execute(deleteQuery,(websiteName,));
        connection.commit();
        print("Deleted information.")
        cursor.close();
        connection.close();
    except:
        sg.popup_error("Couldn't delete the information. Please try again.")