#sam tidmarsh
#1/8/25
#multiplication quiz
import random #for questions
global score #starts score
def multi_quiz(number):
    global score#only works if i do this
    score=0#starts score at 0
    while True:#start an infinite loop unless cancelled
        choice=input("Would you like to play or quit?")#if they want to go endless
        if choice=="quit":#if they wannna quit they don't have to
            print("Thank you so much for trying!")
            break#ends infinite loop
        if choice=="play":#runs full code if they wanna play
            number=int(input("How many questions would you like there to be on the quiz?"))#choice of how many questions they want
            name=input("Please enter your name: ")#be friendly
            print("Welcome to the Multiplication Quiz "+name+"!")
            print("You will be answering "+str(number)+" questions on this quiz! Good Luck!")#tell them how many questions they are answering
            for i in range(number):#run questions for however they chose
                num1=random.randint(1,10)#pick random number 1
                num2=random.randint(1,10)#pick random number 2
                cmp_answer=num1 * num2#computer finds the correct answer
                print("Please solve the problem: "+str(num1)+" * "+str(num2))#find the humans answer to the problem
                hu_answer=int(input("You answer is: "))#gets human answer
                if hu_answer==cmp_answer:#if they get it right
                    print("You got it right!")
                    score=score+1#add to score
                    print("Your score is now: "+str(score))#display score
                else:
                    print("You got it wrong dumbass. The answer was: "+str(cmp_answer)+"!")
                    score=score-1#takes away from score
                    print("Your score is now: "+str(score)+"!")#display lower score


multi_quiz(number)
