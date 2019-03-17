def main():
    title="""          _   _               _       _______        _   
     /\  | | | |             | |     |__   __|      | |  
    /  \ | |_| |__   __ _ ___| |__      | | ___  ___| |_ 
   / /\ \| __| '_ \ / _` / __| '_ \     | |/ _ \/ __| __|
  / ____ \ |_| |_) | (_| \__ \ | | |    | |  __/\__ \ |_ 
 /_/    \_\__|_.__/ \__,_|___/_| |_|    |_|\___||___/\__|
                                                         
                                                         """
    print(title)
    print("\n\nHaving seen the atbash conversion chart, decrypt the following text that has been encrypted using atbash to reveal the password")
    print("Then enter this into the main console to unlock the next level")
    print("\nzgyzhs rh tivzg")
    print("\nYou can use the commands to interact with this pop-up. In this case, typing in \"exit()\" will close the pop-up")
    print("Only do this once you've got the password.")
    print("\nCommands: exit()")
    
    running = True
    while running:
        command = input("Command: ")
        if command=="exit()":
            running=False
        else:
            print("Did not understand that")
main()
