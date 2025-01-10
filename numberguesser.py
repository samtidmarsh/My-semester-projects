#sam tidmarsh
#11/11/24
import random


def numberFinder():
    name = (input("Please enter your name for the game!"))#introduces person
    number = int(input("This is a guessing game! Please enter a number 1-10! Be careful, you only get 3 guesses!"))#first guess
    answer = random.randint(0,10)#makes computer come up with random number
    if number == answer:
        print("You win "+str(name)+ "! Thanks for playing!")#if they get it right
    if number != answer:
        print("So close "+str(name)+"! You only have two more tries!")#if they get it wrong
        secondguess = input("Take another guess!")#second guess
    if secondguess == answer:
        print("Nice guess "+str(name)+"! You win!")#second guess was right
    if secondguess != answer:
        print("So close "+str(name)+"! You only have one more try!")#wrong and third guess
        thirdguess = input("Final guess!")#last one
    if thirdguess == answer:
        print("Great work "+str(name)+"! You win!")#final one was right
    if thirdguess != answer:
        print("So close, but you ran out of guesses "+str(name)+". You were looking to input "+str(answer))#ran out of guesses and told them the right number


numberFinder()
