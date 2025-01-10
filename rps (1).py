#sam tidmarsh
#1/6/24
#rock paper scissors
import random

def game():
    hu_record=0
    cmp_record=0
    print("Welcome to the Rock Paper Scissors Game!")
    while True:#loop
        hu_choice=input("Select rock, paper, scissors, or quit")#ask user what choice
        cmp_choice=random.randint(1,3)#computer choice
        if hu_choice=="quit":#end loop
            break
        if cmp_choice==1:#computer choices personalized
            cmp_choice="rock"
        if cmp_choice==2:
            cmp_choice="paper"
        if cmp_choice==3:
            cmp_choice="scissors"
        if cmp_choice==hu_choice:#when they tie
            print("tie")
        if hu_choice=="rock" and cmp_choice=="paper":#compare with record change
            print("you lose")
            cmp_record=cmp_record+1
        if hu_choice=="rock" and cmp_choice=="scissors":#has them play
            print("you win")
            hu_record=hu_record+1
        if hu_choice=="paper" and cmp_choice=="rock":
            print("you win")
            hu_record=hu_record+1
        if hu_choice=="paper" and cmp_choice=="scissors":
            print("you lose")
            cmp_record=cmp_record+1
        if hu_choice=="scissors" and cmp_choice=="rock":
            print("you lose")
            cmp_record=cmp_record+1
        if hu_choice=="scissors" and cmp_choice=="paper":
            print("you win")
            hu_record=hu_record+1
        print("You chose "+str(hu_choice)+" and the computer chose "+str(cmp_choice)+"!")#shows what person chose and what computer chose
        print("The current record is: You: "+str(hu_record)+" and Computer: "+str(cmp_record))#shows records
game()
