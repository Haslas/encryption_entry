def main():
    title = """   _____ _                                         _           
  / ____| |                                       | |          
 | (___ | |_ ___ _ __   ___   __ _ _ __ __ _ _ __ | |__  _   _ 
  \___ \| __/ _ \ '_ \ / _ \ / _` | '__/ _` | '_ \| '_ \| | | |
  ____) | ||  __/ | | | (_) | (_| | | | (_| | |_) | | | | |_| |
 |_____/ \__\___|_| |_|\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
                              __/ |         | |           __/ |
                             |___/          |_|          |___/ 

"""
    print(title)

    print("\n\nAs said, stenography can be used in the modern day too. And it is. This just in:")
    print("All The Tailors Are Counting Kitchen Nives On Wednesdays")
    print("\nCould that mean anything? Answer in the main console.")
    print("\nCommands: exit()")
    
    running = True
    while running:
        command = input("Command: ")
        if command=="exit()":
            running=False
        else:
            print("Did not understand that")
main()

