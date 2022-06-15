import sqlite3
import os

# Creating the sqlite database
def createDB():
    if os.path.exists(r"/Users/thelevic/code/personal/password-generator/pwmanager"):
        print("Database exists. Continuing.");
    else:
        connection = sqlite3.connect("pwmanager");
        cursor = connection.cursor();
        cursor.execute("CREATE TABLE userinfo (website TEXT, username TEXT, password TEXT)");

def addToDB(website, username, password):
    connection = sqlite3.connect("pwmanager");
    cursor = connection.cursor();
    cursor.execute("insert into userinfo (website, username, password) values (?, ?, ?)",(website, username, password));
    connection.commit();
    connection.close();

def getInfo():
    connection = sqlite3.connect("pwmanager");
    cursor = connection.cursor();
    rows = cursor.execute("SELECT website, username, password FROM userinfo").fetchall();
    print(rows);

