import secrets
import string

#Global variables
specialChars = "!@#$%^&*";
alphabet = specialChars + string.ascii_letters + string.digits;


# Generating a secure password the user likes
def generateSecurePassword(length):
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password;
    
    
    