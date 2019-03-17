#from cryptography.fernet import Fernet
from os import system
import hashlib
def main():
    #I made this the day before the deadline
    #I don't know if there are bugs :((

        lastPass = ""
        commands = loadMain()
        for command in commands:
            try:
            #why doesn't python have switch/case??
                if command[0] == "t":
                    showTextDoc(int(command[1:]))    
                elif command[0] == "i":
                    showImage(command[1:])
                elif command[:2] == "pr":
                    prompt(command[2:])
                elif command[:3] == "sim":
                    lastPass = startSim(command[3:])
                elif command == "ps":
                    pause()
                elif command == "ln":
                    newLine()
                elif command == "f":
                    showFirstTextDoc()
                elif command[:2] == "ut":
                    showUnencryptedText(command[2:])
            except:
                print("Oh no an error")
        end()    
    
def loadMain():
    """
    f = load first text doc
    ps = pause
    t# = show text doc #
    p# = prompt printing #
    sim# = start simulation #
    i# = show image#
    ln = new line
    ut# = sshow other text#
    """
    mainData = loadFile("main_data\\mainData.txt")
    commands = mainData.split("\n")
    return commands

def showFirstTextDoc():
    file = loadFile("text_docs\\first.txt")
    print(file)

def newLine():
    print("")

def showTextDoc(index):
    hashNum = loadFile("hash_codes\\hash"+str(index)+".txt")
    hashPass = 0
    while(hashPass!=hashNum):
        password = input("\nPassword: ").lower()
        hashPass = str(hashPassword(password))
        if(hashPass == hashNum):
            ciphertext = loadFile("text_docs\\text"+str(index)+".txt")
            #plaintext = decryptText(ciphertext, password)
            #print("\n\n"+plaintext)
            print(ciphertext)
        else:
            print("Incorrect Password")
        
def showImage(index):
    file = loadFile("ascii_art\\i"+str(index)+".txt")
    print(file)
    
def startSim(index):
    system("start " + "simulations\\sim"+str(index)+".py")
    
    
def prompt(text):
    input("\n"+text)

def showUnencryptedText(index):
    #Originally I was going to encrypt later levels
    #I got lazy
    file=loadFile("text_docs\\ut"+str(index)+".txt")
    print(file)
    
def decryptText(ciphertext, password):
    password = password.encode("UTF-8")
    password=urlsafe_b64encode(password)
    bytearray(password)
    cipherSuite = Fernet(password)
    plainText = cipherSuite.decrypt(ciphertext)
    return plainText

def hashPassword(password):
    password=password.upper()
    onlyLetters=""
    for char in password:
        if(65<=ord(char) and ord(char)<=90):
            onlyLetters+=char
    password = onlyLetters
    password = password.encode("UTF-8")
    hashObject = hashlib.sha512(password)
    hexDig = hashObject.hexdigest()
    return hexDig

def loadFile(filepath):
    try:
        file = open(filepath, "r")
        filecontents = file.read()
        file.close()
        return filecontents
    except:
        print("Error: could not open file: "+filepath)
        print("Are you running windows?")

def pause():
    input("Press enter to continue...")

def end():
    input("Press enter to exit...")
main()
