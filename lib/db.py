import sqlite3
import os

# Please put desired filepath below, as well as what you would like to name your database file.

filename = "pwmanager";
filepath = r"filepath goes here" + filename;

# Creating the sqlite database
def createDB():
    if os.path.exists(filepath):
        print("Database exists. Continuing.");
    else:
        connection = sqlite3.connect(filepath);
        cursor = connection.cursor();
        cursor.execute("CREATE TABLE userinfo (website TEXT, username TEXT, password TEXT)");
        connection.close();

# Adding information to database
def addToDB(website, username, password):
    connection = sqlite3.connect(filepath);
    cursor = connection.cursor();
    cursor.execute("insert into userinfo (website, username, password) values (?, ?, ?)",(website, username, password));
    connection.commit();
    connection.close();

#Getting information based on the website name
def getInfo(websiteName):
    try:
        connection = sqlite3.connect(filepath);
        cursor = connection.cursor();
        selectQuery = """select * from userinfo where website = ?""";
        cursor.execute(selectQuery,(websiteName,));
        record = cursor.fetchone();
        print("Website: ", record[0]);
        print("Username: ", record[1]);
        print("Password: ", record[2]);
        cursor.close();
        connection.close();
    except:
        print("Failed to get information. Please try again.")

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
        print("Couldn't delete information.")