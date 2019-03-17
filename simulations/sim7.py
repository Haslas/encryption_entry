title="""
  ______       _                          _____ _                 _       _             
 |  ____|     (_)                        / ____(_)               | |     | |            
 | |__   _ __  _  __ _ _ __ ___   __ _  | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __ 
 |  __| | '_ \| |/ _` | '_ ` _ \ / _` |  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
 | |____| | | | | (_| | | | | | | (_| |  ____) | | | | | | | |_| | | (_| | || (_) | |   
 |______|_| |_|_|\__, |_| |_| |_|\__,_| |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
                  __/ |                                                                 
                 |___/                                                                  
"""

def main():
    print(title)
    print("\n(Not mine)")

    print("\n\nIntelligence has come through with the encryption key of a ciphertext we intercepted last week.")
    print("Rotor I = E, Rotor II = V, Rotor III = U")
    print("Switchboard: K=S, A=E")
    print("Ciphertext: CUXIPDIUZSUNTJAYFSOUYB")
    print("Don't copy and paste the ciphertext into the simulation - for full effect type each character individually")

    print("\nVisit this site to carrry out simulation:")
    print("(my ascii characters really wouldn't do it justice)")
    print("http://www.enigmaco.de/enigma/enigma.html")
    print("\nCommands: exit()")
    
    running = True
    while running:
        command = input("Command: ")
        if command=="exit()":
            running=False
        else:
            print("Did not understand that")
main()

