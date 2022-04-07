def user_input():
    possible_input = ["too big", "too small", "you won"]

    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['too big', 'too small', 'you won']")

    return user_answer


def game():
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


if __name__ == '__main__':

    game()