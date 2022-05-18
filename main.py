def user_input():
    
    """
    Function checks if user answer is in 'possible_input' list.
    """
    
    possible_input = ["too big", "too small", "you won"]

    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['too big', 'too small', 'you won']")

    return user_answer


def game():
    
    """
    Main function of our game.
    """
    
    print("Imagine number between 1 and 1000 and I'll try to guess it")
    print("Press 'Enter' to continue: ")
    input()

    max_num = 1000
    min_num = 0
    user_answer = ""

    while user_answer != "you won" :
        guess = (max_num - min_num) // 2 + min_num

        print(f"Your number is: {guess}")
        user_answer = user_input()
        if user_answer == "too big":
            max_num = guess
        elif user_answer == "too small":
            min_num = guess
    print("Hurra I guessed the number !")


print(game())
