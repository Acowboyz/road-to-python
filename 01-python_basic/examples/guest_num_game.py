import random

def random_gen_num():
    return random.randint(1,50)

def guess_num(target_num):

    guess_time = 0
    guessed_list = []

    print("="*50)
    print("Welcome to the GuessNumber game !!!")
    print("You have three time to guess the number.")

    while guess_time < 3:

        try:
            guess_num = int(input("Please guess the target number (1~50):"))
        except ValueError:
            print("This is not a int value !!!")
            continue

        if not 1 <= guess_num <= 50:
            print("The number need to be in 1 ~ 50 !")
        elif guess_num in guessed_list:
            print("You already guessed that !")
        elif guess_num != target_num:
            guessed_list.append(guess_num)
            guess_time += 1 
        else:
            print("Congratulations !!! The answer is %d"%target_num)
    else:
        print("Sorry !!! The answer is %d"%target_num)


def main():
    while True:
        guess_num(random_gen_num())

        response = input("Do you want to play again ? y/n ").lower()
        
        if response == 'y':
            continue
        else:
            break

    print("See you next time.")
    print("="*50)
    
    
if __name__ == "__main__":
    main()
