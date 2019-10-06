import random

#print the instructions

print("lets play a game of Rock paper scissor")

while True:
    print("enter choice \n 1.>Rock \n 2.>Paper \n 3> Scissor")
    #user input
    choice = input("enter your guessed")
    #build a condition to lo0p is option is incorrect
    while choice < 1 or choice >3:
        choice = int(input("invald option"))
        #getting choice choice value
        if choice ==1:
            choice_name='Rock'
        elif choice ==2:
            choice_name='Paper'
        else:
            choice_name='Scissor'
        #printing user choice
        print("user choice is :"+choice_name)
        print("computer turn")
        #computer chooses randomly by ising randint method
        comp_choice =random.randint(1,3)
        # getting comp_choice choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissor'
            print("computer name is :" + comp_choice_name)

        #condition for game 
        if ((choice==1 and comp_choice==2)or (choice==2 and comp_choice==1)):
            result = "Paper"
        elif ((choice==2 and comp_choice==3)or (choice=3 and comp_choice==2)):
            result ="Scissor"
            else:
                result = "Rock"
            #print winner
            if(result ==choice_name):
                print("user is the winner")
            else:
                print("computer wins")
