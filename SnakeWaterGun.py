import random
print("Snake - Water - Gun Game")
n = int(input("Enter the number of rounds :"))
options = ['s' , 'w', 'g']
rounds = 1
comp_win = 0
user_win = 0

while(rounds <= n):
    print(f"\n\nRound : {rounds} \n\n Snake -  ' s '\n Water -  ' w '\n Gun   -  ' g '\n")
    
   #try:
        
    player = input("Choose your option : ")
    '''
    except EOFError as e:
        print(e)
    '''
    if player != 's' and player != 'w' and player != 'g':
        print("Invalid input")
        continue
    computer = random.choice(options)
    
    if computer == 's':
        if player == 'w':
            comp_win += 1
        elif player == 'g':
            user_win += 1
    elif computer == 'w':
        if player == 'g':
            comp_win += 1
        elif player == 's':
            user_win += 1
    elif computer == 'g':
        if player == 's':
            comp_win += 1
        elif player == 'w':
            user_win += 1
    
    if comp_win > user_win:
        print(f"\nComputer Won round {rounds}")
    elif user_win > comp_win:
        print(f"\nUser Won round {rounds}")
    else:
        print("\nDraww!!")
    
    rounds += 1
if comp_win > user_win:
    print("\nYou lost!! try again!!")
elif user_win > comp_win:
    print("\nCongratulations!! You Won!! Play Again!!")
else:
    print("\nMatch Draww!!")

            
