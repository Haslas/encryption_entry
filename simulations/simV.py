def main():
    print(" "*20 + "VIGENERE SQUARE")
    #A = 65, Z = 90
    #make top row:
    print("    ",end="")
    for num in range(65, 91):
        print(chr(num), end=" ")
        
    #make line break:
    print("\n  ",end="")
    for num in range(26):
        print("--",end="")
    print("")
    
    #make rest of rows
    for row in range(26):
        print(chr(row+65)+" | ", end="")
        for num in range(26):
            shifted = num+row
            print(chr((shifted%26)+65), end=" ")
        print("")

    print("Either side can be plaintext character and key character.")
    print("Characters inside of grid are ciphertext characters")

    print("\nCommands: exit()")
    running = True
    while running:
        command = input("Command: ")
        if command=="exit()":
            running=False
        else:
            print("Did not understand that")
main()

