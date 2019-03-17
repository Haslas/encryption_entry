ciphertext = """QEB ZFMEBO VLR GRPQ ABZOVMQBA HBMQ ZLJJRKFZXQFLK PBZROB CLO QEB JXGLOFQV LC QEB CFOPQ JFIIBKKFRJ XA. FQ TXP AROFKD QEB DLIABK XDB LC FPIXJFZ ZFSFIFPXQFLK QEXQ MOLMBO ZOVMQXKXIVQFZ QBZEKFNRBP, PRZE XP QELPB VLR GRPQ BUBZRQBA, TBOB ABSBILMBA. QEBPB QBZEKFNRBP TBOB ABSBILMBA YV XI-HFKAF, XKA XOXY JXQEBJXQFZFXK, TEL TOLQB OFPXIXE CF FPQFHEOXG XI-JR'XJJX: [QEB] JXKRPZOFMQ CLO QEB ABZFMEBOFKD [LC] ZOVMQLDOXMEFZ JBPPXDBP. QEFP TXP FK XMMOLUFJXQBIV 800YZ, 756 VBXOP XCQBO QEB XPPXPPFKXQFLK LC ZXBPXO. 
MXPPTLOA: ZXBPXO FP SBOV ZLLI"""

title = """
   _____                              _____ _       _               
  / ____|                            / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                             | |                    
                                             |_|                    
"""


def main():
    print(title)
    print("\n\nThis is the encrypted text:")
    print("\n"+ciphertext)
    print("\nUse the commands: displayEnglishCharacterPercentages() displayCiphertextFrequencies() displayCiphertextPercentages() decrypt(shift) exit()")
    print("When using decrypt(shift) replace shift with the number you think the alphabet has been shifted by")
    print("Remember, the most common letters from most to least frequent are: e t a o I n s h r d l c u m w f g y p b v k j x q z")
    print("So, if any encrypted characters are paticuarly frequent, they're likely to be the character that will help you guess the shift.")
    print("")
    running = True
    while running:
        try:
            command=input("Command: ")
            #not bullet proof checking but it'll do:
            if command[:4] == "disp" or command[:4] =="decr" or command[:4] == "exit":
                running = eval(command)
            else:
                print("Didn't understand that")
        except:
            print("Didn't understand that")

def displayCiphertextPercentages():
    displayFreqArray(percentFreqAnalysis(ciphertext))
    return True

def displayCiphertextFrequencies():
    displayFreqArray(freqAnalysis(ciphertext))
    return True

def decrypt(shift):
    print(caesarDecrypt(ciphertext, shift))
    return True

def exit():
    return False

def displayEnglishCharacterPercentages():
    englishFreq=["8.2%","1.5%","2.8%","4.3%","13%","2.2%","2.0%","6.1%","7.0%","0.15%","0.77%","4.0%","2.4%","6.7%","7.5%","1.9%","0.095%","6.0%","6.3%","9.1%","2.8%","0.98%","2.4%","0.15%","2.0%","0.074%"]
    displayFreqArray(englishFreq)
    return True

def freqAnalysis(ciphertext):
    freqArray = [0 for num in range(0,26)]
    for char in ciphertext.upper():
        if(ord(char)>=65 and ord(char)<=90):
            freqArray[ord(char)-65]+=1
    return freqArray

def percentFreqAnalysis(ciphertext):
    freqArray = freqAnalysis(ciphertext)
    onlyLetters = ""
    for char in ciphertext.upper():
        if(ord(char)>=65 and ord(char)<=90):
            onlyLetters+=char
    length = len(onlyLetters)
    percentArray = [0 for num in range(0,26)]
    for num in range(0,26):
        percentArray[num] = round(((freqArray[num] / length)*100), 3)

    return percentArray
    

def displayFreqArray(freqArray):
    for num in range(0,26):
        print(" | "+chr(num+65)+" : "+str(freqArray[num]), end="")
    print(" |")


def caesarDecrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext.upper():
        if(ord(char)>=65 and ord(char)<=90):
            newChar = chr(((ord(char)-65+shift)%26)+65)
            plaintext+=newChar
        else:
            plaintext+=char
    return plaintext


main()
