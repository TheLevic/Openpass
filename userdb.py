import sqlite3
import os

filename = "pwmanager";
filepath = r"/Users/thelevic/code/personal/password-generator/" + filename;

# Creating the sqlite database
def createDB():
    if os.path.exists(filepath):
        print("Database exists. Continuing.");
    else:
        connection = sqlite3.connect(filepath);
        cursor = connection.cursor();
        cursor.execute("CREATE TABLE userinfo (website TEXT, username TEXT, password TEXT)");
        connection.close();

def addToDB(website, username, password):
    connection = sqlite3.connect(filepath);
    cursor = connection.cursor();
    cursor.execute("insert into userinfo (website, username, password) values (?, ?, ?)",(website, username, password));
    connection.commit();
    connection.close();

def getInfo():
    connection = sqlite3.connect(filepath);
    cursor = connection.cursor();
    rows = cursor.execute("SELECT website, username, password FROM userinfo").fetchall();
    print(rows);

