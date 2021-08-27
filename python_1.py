import random

print("||       //\\      ||  ||=======  ||        ||======== ||=========||  ||\      /||  ||========    \n")
print("||      //  \\     ||  ||         ||        ||         ||         ||  || \    / ||  ||            \n")
print("||    //     \\    ||  ||         ||        ||         ||         ||  ||  \  /  ||  ||            \n")
print("||   //       \\   ||  ||=====    ||        ||         ||         ||  ||   \/   ||  ||=====       \n")
print("||  //         \\  ||  ||         ||        ||         ||         ||  ||        ||  ||            \n")
print("|| //           \\ ||  ||         ||        ||         ||         ||  ||        ||  ||            \n")
print("||//             \\||  ||======== ||======= ||======== ||=========||  ||        ||  ||========    \n")


def UserIn_for_overs():
    print("-------------------------------------------------------------")
    n=input("Enter the no of overs: ")
    return n


def random_Int_for_score(over):
    # n = random.randint(0,over*36)
    n=13
    return n


def random_Int_for_bat():
    # print("\nComputer's number: ")
    # n=random.randint(0,6)
    n=input("\nComputer's number: ")

    return n


def UserIn_for_bat():
    n=input("\nEnter number to bat: ")
    return n


def working():
    overs = UserIn_for_overs()
    rand_score = random_Int_for_score(int(overs))
    print("\nComputer has scored: %s runs. Your target %d runs. " %(rand_score,int(rand_score)+1))
    Turns = int(overs)*6
    score=0
    over=1
    ball=1
     
    while(Turns>=1):
        Turns-=1
        print("-----------------------------------------------------------------")
        print("\n\nover %s Ball %s" %(over,ball))
        ball+=1
        if(int(ball)==7):
            over+=1
            ball=1
        
        user_bat = UserIn_for_bat()
        rand_bat = random_Int_for_bat()

        if(user_bat==rand_bat):
            print("\nTotal Runs: ",score)
            if(int(rand_score)!=int(score)):
                print("\nYou are out\n\n Computer Won the game by %d runs."  %(int(rand_score)-int(score)))
            else:
                print("\nThis is a draw.")
            break


        else:
            score+=int(user_bat)
            print("Total Runs: ",score)

        if(score>rand_score):
            print("\nTotal Runs: ",score)
            print("\nComputer is out\n\n You Won the game by %d runs."  %(int(score)-int(rand_score)))
            break
        if(Turns==0):
            if(int(rand_score) > int(score)):
                print("\nYou are out\n\n Computer Won the game by %d runs."  %(int(rand_score)-int(score)))
            elif(int(score) > int(rand_score)):
                print("\nComputer is out\n\n You Won the game by %d runs."  %(int(score)-int(rand_score)))
            else:
                print("\nThis is a draw")


def restart_game():
    
    restart = input("\n\nDo you want to play again?(yes/no):\n>>").lower()
    if restart == "yes":
        main()

    else:
        exit()

def main():
    working()
    restart_game()


main()