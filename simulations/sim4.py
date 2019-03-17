from os import system

ciphertext = "IRTQS ITO PCJ CPFS PKCS"
key = "igloo"

title ="""
 __      ___                                  ______                           _      
 \ \    / (_)                                |  ____|                         | |     
  \ \  / / _  __ _  ___ _ __   ___ _ __ ___  | |__  __  ____ _ _ __ ___  _ __ | | ___ 
   \ \/ / | |/ _` |/ _ \ '_ \ / _ \ '__/ _ \ |  __| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \
   
    \  /  | | (_| |  __/ | | |  __/ | |  __/ | |____ >  < (_| | | | | | | |_) | |  __/
     \/   |_|\__, |\___|_| |_|\___|_|  \___| |______/_/\_\__,_|_| |_| |_| .__/|_|\___|
              __/ |                                                     | |           
             |___/                                                      |_|
"""

def main():
    print(title)

    print("\n\nWe have it under good authority that the ciphertext:")
    print(ciphertext)
    print("Was created using the key: ")
    print(key)
    print("\nDecrypt it the cipher using the key to reveal the password.\n")

    running = True
    print("Commands: launchVigenereSquare() exit()")
    while running:
        command = input("Command: ")
        if command == "launchVigenereSquare()" or command == "exit()":
            running = eval(command)
        else:
            print("Command not recognised")

def launchVigenereSquare():
    try:
        system("start simulations\\simV.py")
    except:
        system("start simV.py")
    return True

def exit():
    return False


main()
