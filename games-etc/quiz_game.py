print("Welcome to my computer quiz!")

playing = input("Do you wont to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("What does CPU Stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score +=1
else: 
    print("Incorrect!")


answer = input("What does GPU Stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
else: 
    print("Incorrect!")
    score +=1

answer = input("What does RAM stand for? ")
if answer.lower() == "randon access memory":
    print("Correct")
else: 
    print("Incorrect!")
    score +=1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct")
    score +=1
else: 
    print("Incorrect!")

print ("You got " + str(score) + "Questions Correct!")
print ("You got " + str((score/4) * 100) + "%")
    