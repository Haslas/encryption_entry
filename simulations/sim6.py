import hashlib
title="""
  _____               ____        _     
 |  __ \             / __ \      (_)    
 | |__) |__  _ __   | |  | |_   _ _ ____
 |  ___/ _ \| '_ \  | |  | | | | | |_  /
 | |  | (_) | |_) | | |__| | |_| | |/ / 
 |_|   \___/| .__/   \___\_\\__,_|_/___|
            | |                         
            |_|                         
"""

#The password is the combination of the un-hashed answers
hashedAnswers = ['3787aa805615d57b2f511dc1af9102a0b8164a8ae8d2159692a9d4cc9e033a13d45516ba789bbfe1b9455b1a3641e87ed1101c8b70574591f63e4a0e74983b46',
                 'e50f1295375dc64b15cb533251d6fbe3e868eb01091e223b8f864285f6b045ce8004ffaf678eb89af689e9b8599461f140486308b19deedbc1f1910d421ad6de',
                 'b89ac1aaf8abeffd1449785a9cfce633ab6fb331dd672cfa1ea212bdb01533fe917ec7ad9d9139ad7021dfb09cab964751588f3bf2f7ea3a73107fa4a9cd8e96',
                 '99f97d455d5d62b24f3a942a1abc3fa8863fc0ce2037f52f09bd785b22b800d4f2e7b2b614cb600ffc2a4fe24679845b24886d69bb776fcfa46e54d188889c6f'
    ]
#So doesn't matter that this is here?

questions=["Who wanted steam to do their maths for them?",
           "What is the earliest known cipher?",
           "In what century was the Vigenere Cipher developed? (in the form ____eenth )",
           "What is the second most frequent letter in the English Alphabet? (in the form _ )"]



def main():
    print(title)
    print("\n\nAll of the answers have been stated in this program.")
    print("But you'll probably still end up googling them.")
    input("Press enter to start quiz...")
    print("\n")
    answers=quizLoop()
    password=""
    for answer in answers:
        password+=answer.replace(" ","") #pesky babbage
    print("YOU FINISHED THE POP QUIZ")
    print("password: "+password)
    print("\nCommands: exit()")
    
    running = True
    while running:
        command = input("Command: ")
        if command=="exit()":
            running=False
        else:
            print("Did not understand that")



def quizLoop():
    answers=[]
    index=0
    #try and catch everywhere beacuse I don't have time for bug catching
    try:
        for index in range(0, len(questions)):
            correct=False
            while not correct:
                print(questions[index])
                answer=input("Answer: ")
                hashedAnswer = hashAnswer(answer)
                if hashedAnswer == hashedAnswers[index]:
                    correct=True
                    answers.append(answer)
                    print("Correct!")
                else:
                    print("Incorrect")
    except:
        print("There was an error but it's all okay now")
            
    return answers


def hashAnswer(answer):
    answer=answer.lower()
    answer = answer.encode("UTF-8")
    hashObject = hashlib.sha512(answer)
    hexDig = hashObject.hexdigest()
    return hexDig
main()
