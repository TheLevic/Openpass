import sqlite3
import os

filename = "pwmanager";
filepath = r"C:\Users\Levi\Desktop\Coding_and_Cybersec\Code\password-generator\\" + filename;

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

def getInfo():
    connection = sqlite3.connect(filepath);
    cursor = connection.cursor();
    rows = cursor.execute("SELECT website, username, password FROM userinfo").fetchall();
    print(rows);

#Getting information based on the website name
def betterGetInfo(websiteName):
    try:
        connection = sqlite3.connect(filepath);
        print("Connected!")
        cursor = connection.cursor();
        select_query = """select * from userinfo where website = ?""";
        cursor.execute(select_query,(websiteName,));
        print("executed")
        record = cursor.fetchone();
        print("Website: ", record[0]);
        print("Username: ", record[1]);
        print("Password: ", record[2]);
        cursor.close();
        connection.close();
    except:
        print("Failed to get information. Please try again.")
