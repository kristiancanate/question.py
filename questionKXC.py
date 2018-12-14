answered = False
answer = int (0)

print ("Hello, and welcome to my one question quiz.")
print ("In this program, you will be asked one question and given four options")
print ("to choose from.")
print ("To answer, you will enter the number associated to the option.")
print ("When you are ready to answer the question, hit enter.")
input ("")

while answered == False:
    try:
        print ("QUESTION")
        print ("OPTION 1")
        print ("OPTION 2")
        print ("OPTION 3")
        print ("OPTION 4")
        answer = int (input (""))
        if answer == 2:
            print ("You are correct!")
            answered = True
        elif 0 < answer < 5:
            print ("You are wrong.")
            answered = True
        else:
            print ("ERROR")
    except ValueError:
        print ("ERROR")
