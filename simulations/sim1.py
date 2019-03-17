unwound = """
_______________________

t k a r p s u l e c e !
_______________________
"""

scytale1="""
      | |a| |l|  |
      |t| |s| |  |
   ---| |r| |e|--
   |  |k| |u| |
   |  | |p| |c|
"""
scytale2="""
      |t| |s| |  |
      | |r| |e|  |
   ---|k| |u| |--
   |  | |p| |c|
   |  |a| |l| |
"""


scytale3="""
      | | | | |  |
      |t|r|u|c|  |
   ---|k|p|l|e|--
   |  |a|s|e|!|
   |  | | | | |
(this one seems to fit well)
"""


def main():
    title = """


   _____            _        _         _____                    _       
  / ____|          | |      | |       / ____|                  | |      
 | (___   ___ _   _| |_ __ _| | ___  | (___   ___  ___ _ __ ___| |_ ___ 
  \___ \ / __| | | | __/ _` | |/ _ \  \___ \ / _ \/ __| '__/ _ \ __/ __|
  ____) | (__| |_| | || (_| | |  __/  ____) |  __/ (__| | |  __/ |_\__ \
  
 |_____/ \___|\__, |\__\__,_|_|\___| |_____/ \___|\___|_|  \___|\__|___/
               __/ |                                                    
              |___/                                                     
"""

    print(title)
    print("\n\nThis strip of fabric has been found:")
    print("\n"+unwound)
    print("\nWe have three possible scytales it could fit. When its put on the correct scytale, it will show the password, and be readable from left to right.")
    print("Once you've found the message, input the revealed password into the other console")
    print("Use the commands: showUnwound() wrapAroundScytale1() wrapAroundScytale2() wrapAroundScytale3() exit()")
    running = True
    while(running):
        try:
            command = input("Command: ")
            #good enough security:
            if command[:4] == "wrap" or command[:4] == "exit" or command[:4] == "show":
                running=eval(command)
            else:
                print("Did not understand that")
        except:
            print("Did not understand that")
        

def showUnwound():
    print(unwound)
    return True
def wrapAroundScytale1():
    print(scytale1)
    return True
def wrapAroundScytale2():
    print(scytale2)
    return True
def wrapAroundScytale3():
    print(scytale3)
    return True
def exit():
    return False
main()
