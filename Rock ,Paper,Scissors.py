import random
R = ["rock", "paper", "scissors"]
C = input('Do you want to play Rock,Paper,Scissors [Yes/No] : ')
while C.lower() != 'no':
    P = random.choice(R)
    value = str(input("rock,paper,scissors : "))
    print("Computer's choice is ", P)
    if P == value:
        print("It's a tie")
        r = input('Do you want to play again[Y/N] ')
        if r.lower() == 'y':
            continue
        else:
            break
    elif P == R[0] and value == R[1] or P == R[1] and value == R[2] or P == R[2] and value == R[0]:
        print("You won!")
        r = input('Do you want to play again[Y/N] ')
        if r.lower() == 'y' :
            continue
        else:
            break
    elif P == R[1] and value == R[0] or P == R[2] and value == R[1] or P == R[0] and value == R[-1] :
        print('You lose try again')
        r = input('Do you want to play again[Y/N] ')
        if r.lower() == 'y':
            continue
        else:
            break


